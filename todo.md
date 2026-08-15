# Public Hugo Theme Readiness TODO

## 1. Public metadata + docs

- [x] Fill out `theme.toml` with production-ready metadata:
  - [x] `name`
  - [x] `license`
  - [x] `licenselink`
  - [x] `description`
  - [x] `homepage`
  - [x] `demosite`
  - [x] `tags`
  - [x] `features`
  - [x] realistic `min_version`
  - [x] author homepage
  - [x] original/fork attribution if applicable
- [x] Write a complete `README.md`:
  - [x] screenshot/demo link
  - [x] feature list
  - [x] Hugo Modules installation
  - [x] git submodule installation fallback
  - [x] minimum Hugo version
  - [x] quick-start config
  - [x] content structure examples
  - [x] supported params
  - [x] menu config
  - [x] social config
  - [x] custom CSS/JS support
  - [x] deployment notes
  - [x] license/attribution notes
- [ ] Add real screenshots before publishing to a theme gallery *(deferred; Anurag will add these later)*:
  - [ ] `images/screenshot.png`
  - [ ] `images/tn.png`
- [x] Clarify license and attribution:
  - [x] Decide whether this is a fork/derivative of `hugo-sustain`
  - [x] Update `LICENSE.md` copyright if needed
  - [x] Fill `[original]` in `theme.toml` if needed
  - [x] Mention attribution in `README.md`

## 2. Genericize templates

- [x] Remove personal hardcoding from `layouts/index.html`:
  - [x] Replace `Hi, I'm Anurag.` with configurable/site content
  - [x] Replace Delivery Hero/current-role copy with configurable/site content
- [x] Remove hardcoded brand from `layouts/partials/header.html`:
  - [x] Use `.Site.Title` or `.Site.Params.brand`
- [x] Remove hardcoded copyright from `layouts/partials/footer.html`:
  - [x] Use `.Site.Params.author`, `.Site.Params.copyright`, or `.Site.Title`
- [x] Rework `layouts/_default/resume.html`:
  - [x] Move personal resume content out of the theme
  - [x] Decide whether resume is data-driven, content-driven, or example-only
- [x] Improve `layouts/_default/list.html`:
  - [x] Replace hardcoded `Titles` heading with `.Title` or configurable section title
- [x] Make project layout more reusable:
  - [x] Document expected `data/projects.yml` schema
  - [x] Add defensive logic for missing project data

## 3. Modernize Hugo compatibility

- [x] Replace deprecated config usage:
  - [x] Use `locale` instead of `languageCode` in examples
  - [x] Use `.Site.Language.Locale` instead of `.Site.Language.LanguageCode`
  - [x] Replace `.Site.Data` usage with `hugo.Data` where appropriate
- [x] Replace `.Site.BaseURL` string concatenation:
  - [x] Use `relURL` for local CSS, JS, favicon, navbar, and custom assets while preserving external custom asset URLs
- [x] Ensure the theme and consuming website build warning-free on Hugo `0.165.0`
- [x] Define a minimum supported Hugo version of `0.165.0`

## 4. Fix `exampleSite`

- [x] Update `exampleSite/config.toml`:
  - [x] Remove stale `theme = "hugo-sustain"`
  - [x] Use this theme name/module path
  - [x] Replace personal Anurag-specific values with the `Minimalistic Demo` identity
- [x] Add module-first example support:
  - [x] Add `exampleSite/go.mod`
  - [x] Keep a committed local `replace` so fresh clones build the example from the parent theme checkout
- [x] Replace old default Hugo sample posts with three concise, theme-focused demo posts
- [x] Add representative pages:
  - [x] homepage demo
  - [x] blog list
  - [x] blog posts
  - [x] projects page
  - [x] optional resume page
- [x] Add sample `data/projects.yml` with three generic project entries
- [x] Verify the module-first example build:

```bash
hugo --source exampleSite --gc --minify --panicOnWarning --noBuildLock
```

## 5. Modernize frontend

- [ ] Replace or upgrade old frontend dependencies:
  - [ ] Bootstrap `4.0.0-beta.2`
  - [ ] Font Awesome `4.7.0`
  - [ ] jQuery `3.2.1 slim`
  - [ ] Popper `1.12.3`
  - [ ] Highlight.js `9.7.0`
- [ ] Remove IE10 viewport workaround unless explicitly supported
- [ ] Prefer Hugo Chroma for syntax highlighting
- [ ] Consider Hugo Pipes for CSS/JS:
  - [ ] move assets to `assets/`
  - [ ] minify
  - [ ] fingerprint
  - [ ] cache-bust
- [ ] Improve accessibility:
  - [ ] add accessible labels to icon-only social links
  - [ ] add `rel="noopener noreferrer"` for `target="_blank"`
  - [ ] use HTTPS social URLs
  - [ ] add active/current nav state
- [ ] Make styling configurable:
  - [ ] accent color
  - [ ] font options
  - [ ] optional dark mode

## 6. CI/release readiness

- [x] Add `.gitignore`:
  - [x] `.DS_Store`
  - [x] `.hugo_build.lock`
  - [x] `public/`
  - [x] `resources/`
  - [x] `node_modules/`
- [ ] Add GitHub Actions workflow:
  - [ ] build `exampleSite`
  - [ ] run Hugo with `--gc --minify`
  - [ ] test latest Hugo
  - [ ] optionally test minimum supported Hugo
- [ ] Add release/tag guidance:
  - [ ] first tag, e.g. `v0.1.0`
  - [ ] instructions for consuming via Hugo Modules
  - [ ] instructions for local development using `replace`
- [ ] Verify clean fresh-clone workflow:
  - [ ] clone theme repo
  - [ ] build example site
  - [ ] consume theme from website repo
- [ ] Decide when to remove local `replace` from the website repo and consume a tagged public version
