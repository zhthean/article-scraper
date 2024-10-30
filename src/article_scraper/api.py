
import importlib as _importlib
from typing import cast
from types import ModuleType

from article_scraper.scrapers._bases import BaseScraper
from article_scraper.scrapers._bases import BaseArticle
from article_scraper.utils import scraper_modules


def load_scraper_obj(mod: ModuleType) -> BaseScraper | None:
    for attr in dir(mod):
        if "Scraper" in attr and not attr.startswith("_"):
            scraper_class: BaseScraper = cast(BaseScraper, getattr(mod, attr))
            return scraper_class()

    return None

def scraping(webpages: list[str] | None = None):
    available_scrapers: list[str] = scraper_modules.get_available_scrapers()

    scraper_objs: list[BaseScraper] = []
    for webpage in webpages:
        if webpage not in available_scrapers:
            continue

        mod: ModuleType = _importlib.import_module(name=f".scrapers.{webpage}", package=__package__)
        scraper_obj: BaseScraper = load_scraper_obj(mod)

        if scraper_obj is not None:
            scraper_objs.append(scraper_obj)

    articles: list[BaseArticle] = []
    for obj in scraper_objs:
        obj.scrape()
        obj.retrieve_articles()
        articles.extend(obj.articles)

    for article in articles:
        print(article)
