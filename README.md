# Minimalistic

Minimalistic is a clean Hugo theme for personal websites, blogs, project pages, and lightweight resumes. It started as a personalized fork of `hugo-sustain` and is being separated into a reusable Hugo Module.

> Status: early public-theme cleanup. The theme builds and is usable, but the public API may still evolve before the first tagged release.

## Demo and screenshots

- Demo site: https://anuragaryan.github.io/
- Screenshots are intentionally deferred and are not included yet.

Before publishing the repository to a theme gallery, add a full-size preview at
`images/screenshot.png` and a thumbnail at `images/tn.png`.

## Features

- Minimal personal homepage
- Blog list and single-post layouts
- Related posts by tag
- Projects page backed by `data/projects.yml`
- Optional resume page backed by `data/resume.yml`
- Configurable social links
- Custom CSS and JavaScript hooks
- Responsive Bootstrap-based layout
- Class-based Hugo Chroma syntax highlighting with a GitHub light palette
- Hugo Modules support

## Requirements

- Hugo `0.165.0` or newer
- Go installed when using Hugo Modules

## Installation

### Hugo Modules

In your Hugo site, initialize a Go module if you do not already have one:

```bash
hugo mod init github.com/your-user/your-site
```

Add the theme to your site config:

```toml
[module]

[[module.imports]]
  path = "github.com/anuragaryan/hugo-theme-minimalistic"
```

Then add the module requirement:

```bash
go get github.com/anuragaryan/hugo-theme-minimalistic@latest
```

For local development against a sibling checkout, use a Go module replacement in your site's `go.mod`:

```go
replace github.com/anuragaryan/hugo-theme-minimalistic => ../hugo-theme-minimalistic
```

### Git submodule fallback

If you prefer the traditional Hugo theme workflow:

```bash
git submodule add https://github.com/anuragaryan/hugo-theme-minimalistic.git themes/minimalistic
```

Then set:

```toml
theme = "minimalistic"
```

Do not use both `theme = ...` and `module.imports` for the same theme unless you know exactly why you need both.

## Configuration

A minimal config:

```toml
baseURL = "https://example.com/"
title = "Jane Developer"
locale = "en-US"

[markup]
  [markup.highlight]
    noClasses = false

[module]

[[module.imports]]
  path = "github.com/anuragaryan/hugo-theme-minimalistic"

[params]
  author = "Jane Developer"
  description = "Personal website and technical notes."
  homeTitle = "Hi, I'm Jane."
  homeDescription = "I build reliable software systems and write about engineering."
  copyright = "Jane Developer"
  accentColor = "#27A822"
  darkMode = "auto"
  custom_css = []
  custom_js = []

[params.social]
  Github = "janedev"
  LinkedIn = "janedev"
  Twitter = "janedev"
  Email = "jane@example.com"
  Stackoverflow = "users/123456/jane-dev"
  Instagram = "janedev"

[[menu.main]]
  name = "blog"
  identifier = "blog"
  weight = 100
  url = "/blog/"

[[menu.main]]
  name = "projects"
  identifier = "projects"
  weight = 200
  url = "/projects/"

[[menu.main]]
  name = "resume"
  identifier = "resume"
  weight = 300
  url = "/resume/"
```

## Content model

### Blog posts

Create posts under `content/blog/`:

```toml
+++
title = "My first post"
date = "2026-01-01"
tags = ["hugo", "web"]
+++

Post content goes here.
```

### Projects

Create a page at `content/projects.md`:

```yaml
---
title: "Projects"
showpagemeta: true
---
```

Then configure projects in `data/projects.yml`:

```yaml
name: Projects
source:
  - name: Example Project
    icon: fa-brands fa-github
    url: https://github.com/example/project
    description: A short description of the project.
```

### Resume

Create a page at `content/resume.md`:

```yaml
---
title: "Resume"
isresume: true
---
```

Then configure resume data in `data/resume.yml`:

```yaml
sections:
  - title: Experience
    items:
      - title: Senior Engineer
        subtitle: Example Co.
        date: 2024 – Present
        details:
          - Built reliable systems.
          - Led cross-functional delivery.
  - title: Skills
    items:
      - title: Programming
        details:
          - Go, Python, JavaScript
```

## Customization

### Custom CSS and JavaScript

Add files under your site's `static/` directory and reference them in config:

```toml
[params]
  custom_css = ["css/custom.css"]
  custom_js = ["js/custom.js"]
```

### Social links

The theme supports GitHub, LinkedIn, Twitter/X, StackOverflow, Instagram, and email via `[params.social]`.

### Colors and layout

Set `params.accentColor` to any valid CSS color. It defaults to `#27A822` and is processed into `assets/css/main.css` before Hugo Pipes bundles, minifies, and fingerprints the theme's local styles.

The default font stack is exposed as the `--font-family` CSS custom property. Override it from a stylesheet listed in `params.custom_css`:

```css
:root {
  --font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}
```

If the selected font is not installed locally, load it from the same custom stylesheet or another stylesheet in `params.custom_css`.

Set `params.darkMode` to one of:

- `"auto"` (default): follow the visitor's operating-system preference.
- `"light"`: always use the light palette.
- `"dark"`: always use the dark palette.

Dark mode uses a GitHub dark Chroma palette for highlighted code and requires no client-side JavaScript.

## Deployment

### GitHub Pages

Use Hugo Extended or regular Hugo depending on your build setup. If using Hugo Modules, ensure the build environment has Go installed and runs:

```bash
hugo --gc --minify
```

### Netlify / Cloudflare Pages

Set the build command to:

```bash
hugo --gc --minify
```

Set the publish directory to:

```text
public
```

## Development

Build the example site from this repository:

```bash
hugo --source exampleSite --gc --minify --panicOnWarning --noBuildLock
```

The example site's `go.mod` contains a local `replace` directive pointing to
the parent theme checkout, so this command tests the module-first setup without
fetching a published release.

When using this theme locally from another site, add a `replace` directive in the site's `go.mod`:

```go
replace github.com/anuragaryan/hugo-theme-minimalistic => ../hugo-theme-minimalistic
```

## Releasing

The current public baseline is `v0.1.0`. See [`RELEASING.md`](RELEASING.md) for the clean-clone checks, annotated-tag procedure, GitHub Release command, published-module consumption, and local `replace` workflow for future releases.

## License

MIT. This theme is derived from `hugo-sustain` by Nurlan Su. See `LICENSE.md` and `theme.toml` for attribution details.
