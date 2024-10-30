import argparse

from article_scraper.utils import scraper_modules
from article_scraper import api


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-s",
        "--scrapers",
        choices=scraper_modules.get_available_scrapers(),
        nargs='+',
        type=str,
        default=scraper_modules.get_available_scrapers(),
    )

    return parser.parse_args()  


def main(args):
    api.scraping(webpages=args.scrapers)


if __name__ == "__main__":
    args = parse_args()
    main(args)
