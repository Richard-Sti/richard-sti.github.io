# Richard Stiskalek's website

A Jekyll site hosted on GitHub Pages, styled after [Academic by Paul Le](https://github.com/LeNPaul/academic).
The adaptation keeps Academic's typography, white background, top navigation, two-column introduction, and section dividers, with restrained blue accents and local CSS without Bootstrap or JavaScript navigation.
The upstream reference is commit `5303e549d057dc1a29112e5c38668ffb2725364a`; its MIT licence is preserved in `LICENSE-academic.txt`.

## Local preview

```sh
bundle install
bundle exec jekyll serve
```

Open <http://localhost:4000>.

## Content

- `index.md`: introduction, background, and contact; `<!--more-->` separates the introduction beside the portrait from the full-width sections below.
- `research.md`, `news.md`, `blog.html`, and `cv.md`: existing research, updates, blog links, and full-page PDF CV link.
- `cv.md` forwards the existing `/cv` address to `images/CV.pdf`; the navigation opens the PDF directly.
- `_config.yml`: site identity, contact details, and navigation.
- `css/main.scss`: layout, typography, and responsive styles.
- `_layouts/` and `_includes/`: shared page templates.

## Verification

```sh
bundle exec jekyll build
python3 scripts/check_site.py
```

Pushing `master` triggers the existing GitHub Pages deployment workflow.
The previous Jekyll-Uno site is preserved on `backup/uno-before-academic-2026-09-07` at commit `54e3255`.
