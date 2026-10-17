# Harlequin Dachshunds website

The website for **www.harlequindachshunds.com**, rebuilt in October 2026 from the Wayback Machine copy of the old WordPress site. It looks the same as the original site: same theme, same pages, same text and photos, and the same web addresses.

The site is now plain files with no database, so it can't be lost the way the WordPress site was. GitHub keeps every version of every file, and GitHub Pages hosts it for free.

- **Monthly updates:** see [HOW-TO-UPDATE.md](HOW-TO-UPDATE.md)

---

## Where everything lives

| Folder / file | What's in it |
|---|---|
| `index.html` | Home page |
| `puppies.html`, `about-us.html`, `in-memory.html` | The other main pages |
| `_posts/` | Every dog announcement and blog article, one file each, named `YEAR-MONTH-DAY-name.html` (new ones can be `.md`) |
| `category/` | The Conformation, Agility, Obedience and Blog pages (they fill themselves in from `_posts`) |
| `assets/images/dogs/<name>/` | Photos, one folder per dog |
| `assets/images/puppies/` | Puppy and litter photos |
| `assets/images/site/` | Header banner, logo, AKC badge, About Us photos |
| `assets/images/theme/` | The original theme graphics (purple background, bone buttons, blue ribbons) |
| `_data/navigation.yml` | The menu (pink bone buttons) and footer menu |
| `_data/links.yml` | The "Links" box in the sidebar |
| `_data/comments.json` | Reader comments saved from the old blog |
| `_config.yml` | Site name, email address, location |
| `_layouts/`, `_includes/` | Page templates, copied from the original theme's layout |
| `assets/css/site.css` | The one stylesheet: the original theme's styles (unused WordPress rules removed) plus the site's own additions |
| `assets/js/site.js` | The one script: phone menu and photo viewer |
| `assets/img-sizes/` | Fast WebP copies of every photo in several sizes (made automatically, don't edit) |
| `_data/image_sizes.json` | List of those sizes (made automatically) |
| `tools/optimize_images.py` | Makes the fast photo copies (see HOW-TO-UPDATE.md) |
| `_includes/social-and-schema.html` | Link previews and structured data for Google (filled in automatically) |
| `redirects/` | Keep old links (old `.htm` pages, tag pages) working |
| `CNAME` | Tells GitHub the site's domain name |

Every old web address still works: each post kept its original URL.

---

## One-time setup: putting the site on GitHub Pages

### 1. Create the repository
1. Sign in at https://github.com (or create a free account).
2. Click **+** (top right) → **New repository**. Name it `harlequin-dachshunds` and set it to **Public**. GitHub Pages is free for public repositories. Click **Create repository**.
3. On the next screen, click **uploading an existing file**. Drag in **everything inside** the `harlequin-dachshunds` folder (not the folder itself), including the folders that start with `_`. Click **Commit changes**.
   - Tip: if the drag-and-drop skips folders, install **GitHub Desktop** (https://desktop.github.com), choose *File → Add local repository*, and publish it. That's the most reliable way to upload the whole thing.

### 2. Turn on GitHub Pages
1. In the repository, go to **Settings → Pages**.
2. Under **Build and deployment**, set **Source: Deploy from a branch**, **Branch: main**, folder **/ (root)**, and click **Save**.
3. Under **Custom domain**, enter `www.harlequindachshunds.com` and click **Save**.
4. After about a minute, a green "Your site is live" box appears.

### 3. Point the domain at GitHub
Log in wherever the domain is registered (likely HostGator, or wherever the domain renewal bill comes from) and open the **DNS settings** for harlequindachshunds.com. Then:

| Type | Host / Name | Value |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | `YOUR-GITHUB-USERNAME.github.io` |

Delete any other **A** records for `@`, and any old **CNAME** for `www`, that point to HostGator.
DNS changes take anywhere from a few minutes to 24 hours.

### 4. Turn on HTTPS
Back in **Settings → Pages**, check **Enforce HTTPS** once the option appears. GitHub issues the security certificate automatically, which can take up to an hour after DNS starts working.

### 5. HostGator
- **Keep the domain registration** if it's with HostGator. The domain still needs to renew every year.
- The **hosting plan** is no longer needed for the website. All photos have been recovered from its uploads folder, and your email is Gmail, so it doesn't depend on HostGator. Keep your copy of the uploads zip as a backup.

---

## Previewing changes
After you save a change on GitHub, the live site updates within 1–2 minutes. To check on a build, open the **Actions** tab in the repository: a green check means it published, and a red X means something in the last edit needs fixing. Undo the last change, or ask for help.
