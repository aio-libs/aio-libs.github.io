from pelican import signals
from pelican.contents import Article
from pelican.generator import ArticlesGenerator


def tag_from_path(article_generator: ArticlesGenerator, content: Article) -> None:
    article.tags.append(article.tag)


def register() -> None:
    signals.article_generator_write_article.connect(tag_from_path)
