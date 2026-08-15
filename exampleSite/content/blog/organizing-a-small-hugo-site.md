+++
title = "Organizing a Small Hugo Site"
description = "A practical content structure for a compact personal website."
date = "2026-01-22"
tags = ["hugo", "content", "structure"]
+++

A small Hugo site does not need a complicated content model. A few predictable directories make the project easy to understand and maintain.

## Suggested structure

```text
content/
├── blog/
│   ├── first-post.md
│   └── second-post.md
├── projects.md
└── resume.md

data/
├── projects.yml
└── resume.yml
```

Blog posts hold long-form writing. The projects and resume pages provide routes and introductory content, while their structured entries live under `data/`.

## Keep theme data portable

Avoid putting personal content inside the theme repository. Store it in the consuming site so you can update or replace the theme without moving your writing and profile data.

This separation also makes the theme reusable across multiple sites.
