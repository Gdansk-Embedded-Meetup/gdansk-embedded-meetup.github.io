import logging
import subprocess
import time
import jinja2

from pathlib import Path
from typing import Any
from mkdocs.config.defaults import MkDocsConfig


logger = logging.getLogger("mkdocs.hooks")


def do_startswith(value: str, prefix: str) -> bool:
    return value.startswith(prefix)


def on_env(env: jinja2.Environment, **kwargs: Any) -> None:
    env.tests["startswith"] = do_startswith


def transformPresentation(markdown, page, files, config):
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


def isPresentation(page):
    return page.meta.get("template") == "presentation.html"


def on_page_markdown(markdown, page, files, config, **kwargs):
    if isPresentation(page):
        return transformPresentation(markdown, page, files, config)
    return markdown
