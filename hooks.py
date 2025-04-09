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
