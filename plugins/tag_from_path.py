from typing import Any

from pelican import signals
from pelican.generators import ArticlesGenerator


def tag_from_path(article_generator: ArticlesGenerator, metadata: dict[str, Any]) -> None:
    metadata.setdefault("tags", []).append(metadata["tag"])


def register() -> None:
    signals.article_generator_context.connect(tag_from_path)
