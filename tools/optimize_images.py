#!/usr/bin/env python3
"""Make fast-loading versions of the site's photos.

For every JPG/PNG in assets/images/ (except the small theme graphics) this script:
  1. creates WebP copies at several widths in assets/img-sizes/ (same folder structure),
  2. records the available widths in _data/image_sizes.json (used by _includes/picture.html),
  3. wraps <img> tags in the page and post files in a <picture> element, so each browser
     downloads only the size it needs (phones get small files, desktops larger ones),
  4. makes the first photo on each page load first, and lazy-loads the rest.

The original JPG/PNG files are kept untouched as a fallback.
Safe to run again after adding photos: existing work is skipped.

Usage (from the repository folder):  python3 tools/optimize_images.py
Needs: pip install pillow beautifulsoup4
"""
import glob, json, os, re, sys
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(ROOT, 'assets', 'images')
OUT_DIR = os.path.join(ROOT, 'assets', 'img-sizes')
DATA = os.path.join(ROOT, '_data', 'image_sizes.json')
WIDTHS = [480, 800, 1200, 1600]
SKIP = ('theme/',)
QUALITY = 80

def variant_path(rel, w):
    base, _ = os.path.splitext(rel)
    return f'{base}-{w}.webp'

def make_variants():
    sizes = {}
    for path in sorted(glob.glob(os.path.join(SRC_DIR, '**', '*'), recursive=True)):
        rel = os.path.relpath(path, SRC_DIR).replace(os.sep, '/')
        if not re.search(r'\.(jpe?g|png)$', rel, re.I) or rel.startswith(SKIP):
            continue
        im = Image.open(path)
        w0, h0 = im.size
        widths = [w for w in WIDTHS if w < w0] + [min(w0, WIDTHS[-1])]
        made = []
        for w in sorted(set(widths)):
            out = os.path.join(OUT_DIR, variant_path(rel, w))
            if not os.path.exists(out) or os.path.getmtime(out) < os.path.getmtime(path):
                os.makedirs(os.path.dirname(out), exist_ok=True)
                img = im.convert('RGBA' if im.mode in ('RGBA', 'LA', 'P') and 'transparency' in im.info or im.mode == 'RGBA' else 'RGB')
                if w < w0:
                    img = img.resize((w, round(h0 * w / w0)), Image.LANCZOS)
                img.save(out, 'WEBP', quality=QUALITY, method=6)
            made.append(w)
        sizes['/assets/images/' + rel] = {'w': w0, 'h': h0, 'sizes': made}
    os.makedirs(os.path.dirname(DATA), exist_ok=True)
    json.dump(sizes, open(DATA, 'w'), indent=1, sort_keys=True)
    return sizes

def srcset(src, info):
    rel = src[len('/assets/images/'):]
    return ', '.join(f'/assets/img-sizes/{variant_path(rel, w)} {w}w' for w in info['sizes'])

def sizes_attr(width):
    # Phones: almost full screen width. Larger screens: the photo's set width, capped by the content column.
    return f'(max-width: 600px) 92vw, min({width}px, 62vw)' if width else '(max-width: 600px) 92vw, 62vw'

IMG_RE = re.compile(r'(<picture>\s*<source[^>]*>\s*)?(<img\b[^>]*>)(\s*</picture>)?', re.S)
ATTR = lambda tag, a: (re.search(rf'\b{a}="([^"]*)"', tag) or [None, None])[1]

def rewrite_html(sizes):
    files = [f for f in glob.glob(os.path.join(ROOT, '*.html')) + glob.glob(os.path.join(ROOT, '_posts', '*.*'))
             if not os.path.basename(f).startswith('404')]
    changed = 0
    for f in files:
        text = open(f, encoding='utf-8').read()
        if not text.startswith('---'):
            continue
        end = text.index('\n---', 3) + 4
        head, body = text[:end], text[end:]
        first = [True]

        def fix(m):
            img = m.group(2)
            src = ATTR(img, 'src')
            img = re.sub(r'\s(loading|fetchpriority|decoding)="[^"]*"', '', img)
            if first[0]:
                img = img.replace('<img', '<img fetchpriority="high" loading="eager"', 1)
            else:
                img = img.replace('<img', '<img loading="lazy" decoding="async"', 1)
            first[0] = False
            info = sizes.get((src or '').split('?')[0])
            if not info:
                return img
            width = ATTR(img, 'width')
            source = f'<source type="image/webp" srcset="{srcset(src, info)}" sizes="{sizes_attr(width)}">'
            return f'<picture>{source}{img}</picture>'

        new = IMG_RE.sub(fix, body)
        if new != body:
            open(f, 'w', encoding='utf-8').write(head + new)
            changed += 1
    return changed

if __name__ == '__main__':
    s = make_variants()
    n = rewrite_html(s)
    total = sum(os.path.getsize(p) for p in glob.glob(os.path.join(OUT_DIR, '**', '*.webp'), recursive=True))
    print(f'{len(s)} photos, WebP versions total {total / 1048576:.1f} MB, {n} page/post files updated')
