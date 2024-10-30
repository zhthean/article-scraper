import pkgutil as _pkgutil

from article_scraper import scrapers as _scrapers


def get_available_scrapers() -> list[str]:
    available_scrapers: list[str] = []
    for module in _pkgutil.iter_modules(_scrapers.__path__):
        if module.name.startswith("_"):
            continue

        available_scrapers.append(module.name)

    return available_scrapers
