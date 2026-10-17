# How to update the website

You can make every change below on github.com in a web browser. Each change goes live about 1–2 minutes after you click **Commit changes**.

Text files use **Markdown**, a simple way to format writing:

| You type | You get |
|---|---|
| `## Big heading` | a heading |
| `**bold**` | **bold** |
| `*italic*` | *italic* |
| `[AKC](https://www.akc.org)` | a link |
| `![Molly winning](/assets/images/dogs/molly/molly-win.jpg)` | a photo |
| a blank line | a new paragraph |

---

## Announce a new win or a new dog (the most common update)

**1. Upload the photo**
- Go to `assets/images/dogs/`. Open the dog's folder, or create one by typing `assets/images/dogs/newdogname/photo.jpg` as the file name when uploading.
- Click **Add file → Upload files**, drag in the photo, and click **Commit changes**.
- Use simple file names: lowercase letters, numbers and dashes, no spaces. Example: `molly-best-of-variety-2026.jpg`.
- Photos straight off a phone are fine, but under about 2 MB loads faster.

**2. Create the post**
- Go to the `_posts` folder and click **Add file → Create new file**.
- Name it with the date first: `2026-11-02-molly-best-of-variety.md`
- Paste this in and change the details:

```
---
title: "CH Harlequin Pretty in Pink ML – Best of Variety!"
categories: [conformation]
dog: Molly
image: /assets/images/dogs/molly/molly-best-of-variety-2026.jpg
description: "Molly took Best of Variety at the Hunterdon Hills Kennel Club show."
permalink: /molly-best-of-variety-2026/
---

Molly took **Best of Variety** at the Hunterdon Hills Kennel Club show in November 2026!

![Molly with her Best of Variety ribbon](/assets/images/dogs/molly/molly-best-of-variety-2026.jpg)
```

- `categories` decides which page the post appears on. Use `[conformation]`, `[agility]`, `[obedience]`, or `[blog]`. You can list more than one, like `[agility, obedience]`.
- `permalink` is the post's web address. Make it short and unique.
- Click **Commit changes**. The post shows up at the top of its category page automatically.

**Two photos side by side:**
```
<p><img src="/assets/images/dogs/molly/photo-one.jpg" alt="Molly in the ring" width="400"> <img src="/assets/images/dogs/molly/photo-two.jpg" alt="Molly with the judge" width="400"></p>
```

**A photo with a caption:**
```
<div class="wp-caption aligncenter">
  <img src="/assets/images/dogs/molly/photo.jpg" alt="Molly">
  <p class="wp-caption-text">Molly finished her championship in August 2024.</p>
</div>
```

**Prefer copying an old post?** The existing posts in `_posts` are `.html` files: they're the original WordPress HTML, so they look exactly like the old site. You can copy one, rename it, and change the text and photo names. Either way works.

**A YouTube video:** copy the code at the end of the YouTube link (for `youtube.com/watch?v=U1M74JceAYk` it's `U1M74JceAYk`) and put it in place of `VIDEO-CODE` here:
```
<iframe width="560" height="315" src="https://www.youtube.com/embed/VIDEO-CODE" allowfullscreen></iframe>
```

---

## Keeping new photos fast
The site serves each visitor a right-sized WebP copy of every photo (phones get small files). Those copies are made by `tools/optimize_images.py`.

- **Easiest:** send the new photo to Claude with your update. Claude adds it and makes the fast copies.
- **Yourself (on a Mac with Python):** after adding photos or posts in GitHub Desktop, open Terminal in the site folder and run `python3 tools/optimize_images.py`, then commit and push.
- **If you skip this,** new photos still work: they just load at full size, like before.

Fill in the photo's `alt="..."` with a short description of what's in it (for Google Images and screen readers).

---

## Update the Puppies page (new litter, puppy available, litter placed)
Open `puppies.html`, click the **pencil icon** (Edit), make your changes, and click **Commit changes**.
Puppy photos go in `assets/images/puppies/`.

## Change an existing post or page
Find the file (pages are in the main folder, posts are in `_posts`), click the **pencil icon**, edit, and commit.

## Remove a post
Open the file in `_posts`, click **⋯ → Delete file**, and commit.

## Change the email address, menu or links
- Email, site name, location: `_config.yml`
- Menu (bone buttons): `_data/navigation.yml`
- Sidebar links: `_data/links.yml`

## Made a mistake?
Every version is saved. Open the file and click **History** to see earlier versions. Or ask Claude: "undo my last change to the Harlequin Dachshunds site" or "add this win to the website" works fine. Attach the photo and describe the news.
