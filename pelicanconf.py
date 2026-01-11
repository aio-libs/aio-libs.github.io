import logging
import re
from pathlib import Path

from jinja2 import Environment, FileSystemLoader
from markdown import Markdown
from markdown.extensions import Extension
from markdown.extensions.admonition import AdmonitionExtension
from markdown.extensions.meta import MetaExtension
from markdown.extensions.smarty import SmartyExtension
from markdown.extensions.toc import TocExtension
from markdown.extensions.wikilinks import WikiLinkExtension
from markdown.inlinepatterns import InlineProcessor

jinja_fragments = Environment(loader=FileSystemLoader("theme/templates/fragments/"))
sponsor_template = jinja_fragments.get_template("sponsor.html")
SPONSOR_IMG_PATH = Path("content/images/sponsors/")


def sponsor_img(name: str):
    name = name.lower().replace(" ", "-")
    f = next(SPONSOR_IMG_PATH.glob(name + ".*"))
    return "/images/sponsors/" + f.name


class SponsorInlineProcessor(InlineProcessor):
    def handleMatch(self, m: re.Match[str], data: str) -> tuple[str, int, int]:
        return sponsor_template.render(SPONSORS=SPONSORS), m.start(0), m.end(0)


class SponsorExtension(Extension):
    def extendMarkdown(self, md: Markdown) -> None:
        processor = SponsorInlineProcessor(r'\[\[SPONSORS\]\]', md)
        md.inlinePatterns.register(processor, "sponsor", 200)


SITENAME = "aio-libs"
SITEURL = ""
SUMMARY_MAX_PARAGRAPHS = 1

ARTICLE_PATHS = ("news",)
PATH = "content"

LOCALE = "en_US.utf8"
TIMEZONE = "UTC"

_SPONSORS = (
    ("Tidelift", "https://tidelift.com/"),
    ("Open Home Foundation", "https://www.openhomefoundation.org/"),
)
SPONSORS = tuple({"name": s[0], "img": sponsor_img(s[0]), "url": s[1]} for s in _SPONSORS)

# URL settings
FILENAME_METADATA = r"(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)"
ARTICLE_URL = "news/{date:%Y}/{slug}/"
ARTICLE_SAVE_AS = "news/{date:%Y}/{slug}/index.html"
AUTHOR_URL = "author/{slug}/"
AUTHOR_SAVE_AS = "author/{slug}/index.html"
AUTHORS_SAVE_AS = "author/index.html"
CATEGORY_URL = "category/{slug}/"
CATEGORY_SAVE_AS = "category/{slug}/index.html"
CATEGORIES_SAVE_AS = "category/index.html"
INDEX_SAVE_AS = "news/index.html"
PATH_METADATA = r"pages/(?P<prefix>([^/]+/)|)(?P<slug>.*)\.md"
PAGE_URL = "{prefix}{slug}/"
PAGE_SAVE_AS = "{prefix}{slug}/index.html"
TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"
TAGS_SAVE_AS = "tag/index.html"
YEAR_ARCHIVE_SAVE_AS = "news/{date:%Y}/index.html"
YEAR_ARCHIVE_URL = "news/{date:%Y}/"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Plugins
PLUGIN_PATHS = ("plugins",)
PLUGINS = ("linkclass",)
MARKDOWN = {
    "extensions": (
        "extra",
        AdmonitionExtension(),
        MetaExtension(),
        SmartyExtension(),
        TocExtension(),
        WikiLinkExtension(base_url="/projects/", html_class=None),
        SponsorExtension(),
    ),
}

# Theme
THEME = "theme/"
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/")
)
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10
PAGINATED_TEMPLATES = {"index": None, "tag": None, "category": None, "author": 5}
PAGINATION_PATTERNS = (
    (1, "{url}", "{save_as}"),
    (2, "{base_name}/{number}/", "{base_name}/{number}/index.html"),
)

LOG_FILTER = (
    # Remove when fixed: https://github.com/getpelican/pelican/pull/3544
    (logging.WARN, "Feeds generated without SITEURL set properly may not be valid"),
    # Alt tag is explicit in Markdown, so this warning doesn't make sense.
    (logging.WARN, "Empty alt attribute for image %s in %s"),
)
