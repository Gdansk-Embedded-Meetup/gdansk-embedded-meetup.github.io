import logging
import jinja2

from textwrap import dedent
from typing import Any


logger = logging.getLogger("mkdocs.hooks")


def do_startswith(value: str, prefix: str) -> bool:
    return value.startswith(prefix)


def on_env(env: jinja2.Environment, **kwargs: Any) -> None:
    env.tests["startswith"] = do_startswith


def transformPresentation(markdown, page, files, config):
    if "website" in page.meta:
        github = "https://github.com/"
        if page.meta["website"].startswith(github):
            repo = page.meta["website"].removeprefix(github)
            button = (
                f'\n<p markdown=1 align="center">[:fontawesome-brands-github: {repo}]({page.meta["website"]})'
                "{ .md-button }</p>"
            )
        else:
            button = (
                f'\n<p markdown=1 align="center">[:fontawesome-solid-globe: {page.meta["website"].removeprefix("https://")}]({page.meta["website"]})'
                "{ .md-button }</p>"
            )
        markdown += "\n## Strona projektu"
        markdown += button
    baseUrl = f"{config.repo_url}/blob/main/content/"
    if "attachments" in page.meta:
        markdown += "\n##Załączniki od autora"
        for a in page.meta["attachments"]:
            markdown += f"\n- [{a}]({baseUrl}{page.url}{a})"
    if "youtube_url" in page.meta:
        yt = page.meta["youtube_url"]
        video_id = yt.split("=")[1].split("?")[0]
        markdown += '\n##🎥 Nagranie { data-toc-label="Nagranie" }'
        markdown += f'\n<iframe width="100%" style="aspect-ratio: 16 / 9;" src="https://www.youtube-nocookie.com/embed/{video_id}"'
        markdown += ' title="YouTube video player" frameborder="0"'
        markdown += ' allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"'
        markdown += " allowfullscreen></iframe>"
    if "slides" in page.meta:
        slides = page.meta["slides"]
        markdown += (
            f'\n##🗒️ Slajdy (<a href="{slides}">Fullscreen</a>)'
            ' { #slajdy data-toc-label="Slajdy" }'
        )
        markdown += f'\n<object data="{slides}" type="application/pdf" width="100%" style="aspect-ratio: 16 / 9;"></object>'
    return markdown


def transformEvent(markdown, page, files, config):
    markdown += '\n## 🪧 Prezentacje: { data-toc-label="Prezentacje" }'
    markdown += '\n<div class="events">'
    for f in files:
        if f.url.startswith(page.url) and f.url != page.url and f.page:
            f.page.read_source(config)
            if not f.page.meta.get("tags"):
                # no tags means a presentation page that's actually a summary page with children, e.g. lightning talks session
                continue
            markdown += dedent(f"""
                            <article class="event-article">
                            <div>
                                <h2>
                                <a href="{f.url_relative_to(page.file)}">{f.page.title}</a>
                                </h2>
                            </div>
                            </article>
                            """)
    markdown += "\n</div>"

    if "photos" in page.meta:
        folder = page.meta["photos"]
        folder = folder.split("/")[-1].split("?")[0]
        markdown += '\n##📸 Zdjęcia ze spotkania { #zdjecia data-toc-label="Zdjęcia" }'
        markdown += f"\nWszystkie zdjęcia znajdziesz w [folderze Google Drive](https://drive.google.com/drive/folders/{folder})"
        markdown += dedent(f"""
                        <iframe id="drive-frame" src="https://drive.google.com/embeddedfolderview?id={folder}#grid"
                            style="width:100%; aspect-ratio: 16 / 9; border:0; background-color: transparent; overflow-x:hidden;">
                        </iframe>""")
    return markdown


def isPresentation(page):
    return page.meta.get("template") == "presentation.html"


def isEvent(page):
    return page.meta.get("template") == "event.html"


def on_page_markdown(markdown, page, files, config, **kwargs):
    if isPresentation(page):
        return transformPresentation(markdown, page, files, config)
    if isEvent(page):
        return transformEvent(markdown, page, files, config)
    return markdown
