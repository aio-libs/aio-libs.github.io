from pelican import signals
from pelican.contents import Article
from pelican.generators import ArticlesGenerator


def tag_from_path(article_generator: ArticlesGenerator, content: Article) -> None:
    if not hasattr(content, "tags"):
        content.tags = []
    content.tags.append(content.tag)


def register() -> None:
    signals.article_generator_write_article.connect(tag_from_path)
