+++
title = "Customizing Minimalistic"
description = "Use site parameters and local assets without editing the theme."
date = "2026-01-29"
tags = ["hugo", "customization", "css"]
highlight = true
+++

A reusable Hugo theme should rarely require direct edits. Minimalistic exposes common identity, navigation, social-link, and asset settings through site configuration.

## Add local styles

Place a stylesheet under your site's `static/css/` directory and reference it from the configuration:

```toml
[params]
  custom_css = ["css/custom.css"]
```

You can load scripts in the same way:

```toml
[params]
  custom_js = ["js/custom.js"]
```

Local paths are rendered relative to the site's base path. Fully qualified `http://`, `https://`, and protocol-relative URLs are preserved for external assets.

## Override only when necessary

Hugo lets a consuming site override a theme layout by creating a file at the same path under its own `layouts/` directory. Prefer configuration and custom assets first, then use a layout override for genuinely structural changes.
