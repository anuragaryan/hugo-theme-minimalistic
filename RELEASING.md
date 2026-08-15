# Releasing Minimalistic

The planned first public release is `v0.1.0`. Create the tag only after the clean-clone and consumer-site checks pass.

## Pre-release checklist

1. Start from an up-to-date, clean `master` branch:

   ```bash
   git checkout master
   git pull --ff-only origin master
   git status --short
   ```

2. Confirm the GitHub Actions build is green for both the minimum supported Hugo version and the latest Hugo Extended release.

3. Run the strict example build locally:

   ```bash
   hugo --source exampleSite --gc --minify --panicOnWarning --noBuildLock
   ```

4. Complete the fresh-clone and external consumer-site verification documented in the public-readiness checklist.

5. Review `README.md`, `theme.toml`, the license and release notes for accuracy.

## Create `v0.1.0`

Create an annotated tag from the verified `master` commit:

```bash
git tag -a v0.1.0 -m "Release v0.1.0"
git push origin v0.1.0
```

Then create a GitHub Release from the existing tag:

```bash
gh release create v0.1.0 \
  --verify-tag \
  --title "Minimalistic v0.1.0" \
  --generate-notes
```

Do not move or recreate a published version tag. Fix release issues in a new patch version instead.

## Consume a published release

In the consuming Hugo site's `config.toml`:

```toml
[module]

[[module.imports]]
  path = "github.com/anuragaryan/hugo-theme-minimalistic"
```

Initialize the consumer module if necessary, then request the tagged theme:

```bash
hugo mod init github.com/example/site
hugo mod get github.com/anuragaryan/hugo-theme-minimalistic@v0.1.0
hugo mod tidy
```

Commit the resulting `go.mod` and `go.sum` when one is created. Build the consumer without a local replacement to confirm it resolves the public tag.

## Local theme development

A consumer can temporarily use a sibling theme checkout:

```bash
go mod edit -replace=github.com/anuragaryan/hugo-theme-minimalistic=../hugo-theme-minimalistic
```

The consumer's `go.mod` will contain:

```go
replace github.com/anuragaryan/hugo-theme-minimalistic => ../hugo-theme-minimalistic
```

Before validating a published release, remove the local replacement and request the tag:

```bash
go mod edit -dropreplace=github.com/anuragaryan/hugo-theme-minimalistic
hugo mod get github.com/anuragaryan/hugo-theme-minimalistic@v0.1.0
hugo mod tidy
```
