from pathlib import Path
import tomllib

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text()


def test_theme_metadata_is_public_ready():
    data = tomllib.loads(read("theme.toml"))
    assert data["name"] == "Minimalistic"
    assert data["license"] == "MIT"
    assert data["licenselink"].startswith("https://github.com/anuragaryan/hugo-theme-minimalistic")
    assert data["description"]
    assert data["homepage"] == "https://github.com/anuragaryan/hugo-theme-minimalistic"
    assert data["demosite"]
    assert "personal" in data["tags"]
    assert "blog" in data["features"]
    assert data["min_version"] >= "0.120.0"
    assert data["author"]["homepage"]
    assert data["original"]["repo"]


def test_readme_documents_public_usage():
    readme = read("README.md")
    required = [
        "# Minimalistic",
        "## Features",
        "## Installation",
        "Hugo Modules",
        "git submodule",
        "## Configuration",
        "## Content model",
        "## Customization",
        "## Deployment",
        "## License",
    ]
    for text in required:
        assert text in readme
    assert len(readme.splitlines()) > 80


def test_personal_hardcoding_removed_from_theme_layouts():
    layout_text = "\n".join(path.read_text() for path in (ROOT / "layouts").rglob("*.html"))
    forbidden = [
        "Hi, I'm Anurag.",
        "Delivery Hero",
        "Anurag Aryan",
        "github.com/anuragaryan",
        "linkedin.com/in/anuragaryan",
        "AnuragCodes",
    ]
    for text in forbidden:
        assert text not in layout_text


def test_homepage_header_footer_are_configurable():
    assert ".Site.Params.homeTitle" in read("layouts/index.html")
    assert ".Site.Params.homeDescription" in read("layouts/index.html")
    assert ".Site.Title" in read("layouts/partials/header.html")
    footer = read("layouts/partials/footer.html")
    assert ".Site.Params.copyright" in footer
    assert ".Site.Params.author" in footer


def test_resume_and_projects_are_data_driven_or_defensive():
    resume = read("layouts/_default/resume.html")
    assert "site.Data.resume" in resume or "hugo.Data.resume" in resume
    assert "DELIVERY HERO" not in resume
    assert "VIT UNIVERSITY" not in resume

    projects = read("layouts/_default/projects.html")
    assert "with" in projects
    assert "projects" in projects
    assert "No projects" in projects


def test_example_site_uses_this_theme_and_generic_identity():
    cfg = read("exampleSite/config.toml")
    assert "hugo-theme-minimalistic" in cfg or "minimalistic" in cfg
    assert "hugo-sustain" not in cfg
    assert "Anurag Aryan" not in cfg


def test_asset_urls_use_hugo_helpers_and_allow_external_custom_assets():
    head = read("layouts/partials/head.html")
    scripts = read("layouts/partials/js.html")
    combined = head + scripts

    assert ".Site.BaseURL" not in combined
    for asset in [
        '"img/favicon.ico" | relURL',
        '"css/main.css" | relURL',
        '"css/resume.css" | relURL',
        '"css/blogpost.css" | relURL',
        '"js/ie10-viewport-bug-workaround.js" | relURL',
    ]:
        assert asset in combined

    assert 'strings.HasPrefix $asset "http://"' in head
    assert 'strings.HasPrefix $asset "https://"' in head
    assert 'strings.HasPrefix $asset "//"' in head
    assert "$asset | relURL" in head
    assert 'strings.HasPrefix $asset "http://"' in scripts
    assert 'strings.HasPrefix $asset "https://"' in scripts
    assert 'strings.HasPrefix $asset "//"' in scripts
    assert "$asset | relURL" in scripts


def test_theme_has_no_google_analytics_configuration_or_partial():
    assert "googleAnalytics" not in read("exampleSite/config.toml")
    assert 'partial "google_analytics.html"' not in read("layouts/partials/head.html")
