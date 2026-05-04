# AGENTS.md

## Project Overview

This is the website for **Gdańsk Embedded Meetup** built with **MkDocs** and **Material for MkDocs**. It documents past and upcoming embedded systems meetups in Gdańsk, Poland, including event pages, presentation details, speakers, and sponsors.

## Tech Stack

- **Static site generator**: MkDocs 1.6.1 with Material theme 9.6.11
- **Python package manager**: uv
- **Python version**: ~3.10
- **Custom plugins**: `mkdocs-awesome-nav`, `mkdocs-meta`
- **CI/CD**: GitHub Actions (build on push to `main`, deploy to `gh-pages`)

## Directory Structure

```
content/              # Documentation source (docs_dir)
  events/             # Event pages organized by year
    <year>/
      <yyyy-mm-dd>_<number>/   # Each meetup
        index.md           # Event overview
        1/index.md         # Presentation 1
        2/index.md         # Presentation 2
        static/            # Event-specific assets
  sponsors.md
  organizers.md
  tags.md
  index.md
  stylesheets/extra.css
template_event/2099-01-01_999/   # Template for new events
overrides/              # Custom Jinja2 templates
  event.html
  presentation.html
  event_list.html
  partials/comments.html
mkdocs.yml              # Site configuration
hooks.py                # MkDocs hooks (Jinja filters, markdown transforms)
pyproject.toml          # Project dependencies (managed with uv)
```

## Key Conventions

### Event naming

Events are stored under `content/events/<year>/<yyyy-mm-dd>_<number>/` where `<number>` is the sequential meetup number (e.g., `2025-01-07_026` for the 26th meetup).

### Event page (`index.md`)

- Uses `template: event.html`
- Frontmatter fields: `title`, `date`, `location`, `cover`, `meetup_url`, `photos`
- `location` must match a key from `mkdocs.yml` → `extra.locations` (e.g., `starter`, `nordea`, `sztuka_wyboru`, `d003`, `amber_expo`)
- Hooks in `hooks.py` auto-generate the presentations list and Google Drive photo embeds

### Presentation page (`1/index.md`, etc.)

- Uses `template: presentation.html`
- Frontmatter fields: `title`, `template: presentation.html`, `slides`, `youtube_url`, `tags`, `website`, `attachments`
- `tags` must be from the list in `mkdocs.yml` → `extra.tags`
- Hooks in `hooks.py` auto-render project links, YouTube embeds, PDF slide embeds, and attachment lists

### Adding a new event

1. Copy `template_event/2099-01-01_999` to `content/events/<year>/<yyyy-mm-dd>_<next_number>/`
2. Fill in the event `index.md` (title, date, location, schedule, partners)
3. Create subfolders `1/`, `2/`, etc. for each presentation with their own `index.md`
4. Use the `scrape-event` skill for automating this from a meetup.com URL

### Tags
- tags are handled by the built-in tags plugin
- tags are read dynamically from the pages and don't need to be defined upfront
- some of the tags are explicitly added in `mkdocs.yml` to add custom icons to them
## Commands

```bash
# Install dependencies
uv sync --dev

# Serve with live reload
uv run mkdocs serve --watch-theme

# Build production site (strict mode)
uv run mkdocs build --strict

# Run with strict mode to catch errors during development
uv run mkdocs serve --strict
```

## CI/CD

- **Trigger**: Push to `main` branch
- **Build**: `uv run mkdocs build --strict`
- **Deploy**: Push `dist/` folder to `gh-pages` branch via `JamesIves/github-pages-deploy-action`

## Hooks (hooks.py)

The MkDocs hooks in `hooks.py` provide custom markdown transformations:

- **`transformPresentation`**: Adds project website buttons, YouTube video embeds, PDF slide embeds, and attachment links based on page frontmatter
- **`transformEvent`**: Auto-generates a presentations list from child pages and embeds Google Drive photo galleries
- **`on_env`**: Registers a custom Jinja2 test `startswith`

Templates to check for determining which transform to apply:
- `page.meta.get("template") == "presentation.html"` → `transformPresentation`
- `page.meta.get("template") == "event.html"` → `transformEvent`
