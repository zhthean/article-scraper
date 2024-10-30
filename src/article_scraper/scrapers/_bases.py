from abc import abstractmethod

from bs4 import BeautifulSoup as _BeautifulSoup
import requests as _requests
from selenium.webdriver.remote.webdriver import WebDriver as _WebDriver

from article_scraper.scrapers._interfaces import ArticleInterface as _ArticleInterface
from article_scraper.scrapers._interfaces import NewsScraperInterface as _NewsScraperInterface
from article_scraper.utils.driver import get_driver


class BaseArticle(_ArticleInterface):
    
    def __init__(self, title: str, url: str) -> None:
        self._title = title
        self._url = url
        self._content = ""

    def __str__(self) -> str:
        return f"{self._title}: {self._url}"
    
    @property
    def content(self) -> str:
        return self._content

    def retrieve_content(self, praser: _BeautifulSoup | None = None) -> str:
        response = _requests.get(self._url)
        soup: _BeautifulSoup = praser(response.content, "html.parser") if praser else _BeautifulSoup(response.content, "html.parser")

        prased_result: str = self._process(soup)
        self._content = prased_result

        return self._content

    @abstractmethod
    def _process(soup: _BeautifulSoup) -> str:
        pass


class BaseScraper(_NewsScraperInterface):

    def __init__(self, url: str) -> None:
        self._url = url
        self._article_list = []

    @property
    def articles(self):
        return self._article_list

    def scrape(self, driver: _WebDriver | None = None) -> None:
        driver: _WebDriver = driver if driver is not None else get_driver()
        driver.get(self._url)

        self._extract_data(driver)

        driver.quit()

    def retrieve_articles(self) -> None:
        for article in self._article_list:
            article.retrieve_content()

    @abstractmethod
    def _extract_data(self, driver: _WebDriver):
        pass
