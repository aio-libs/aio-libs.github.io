SITENAME = "aio-libs"
SITEURL = ""
SUMMARY_MAX_PARAGRAPHS = 1

ARTICLE_PATHS = ["news"]
PATH = "content"

LOCALE = "en"

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
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
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

# Theme
#THEME = "theme"
# TODO: LINKS/SOCIAL
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
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


# TODO: Assert date included in all article filenames.
