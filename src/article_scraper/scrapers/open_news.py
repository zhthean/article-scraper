from bs4 import BeautifulSoup as _BeautifulSoup
from selenium.webdriver.remote.webdriver import WebDriver as _WebDriver
from selenium.webdriver.common.by import By

from article_scraper.scraping_parameters import OpenNewsParameters as _Parameters
from article_scraper.scrapers._bases import BaseScraper as _BaseScraper
from article_scraper.scrapers._bases import BaseArticle as _BaseArticle


class OpenNewsArticle(_BaseArticle):

    def __init__(self, title: str, url: str) -> None:
        super().__init__(
            title=title,
            url=url,
        )

    def _process(self, soup: _BeautifulSoup) -> str:
        items = soup.find(_Parameters.ARTICLE_BODY_ELEMENT.value, class_=_Parameters.ARTICLE_BODY_CLASS.value)
        paragraphs = [item.get_text() for item in items.find_all(_Parameters.PARAGRAPH_ELEMENT.value, class_=_Parameters.PARAGRAPH_CLASS.value)]
        clean_paragraphs = [paragraph for paragraph in paragraphs if paragraph]
        result = "\n\n".join(clean_paragraphs)

        return result


class OpenNewsScraper(_BaseScraper):

    def __init__(self) -> None:
        super().__init__(_Parameters.URL.value)

    def scrape(self, driver: _WebDriver | None = None) -> None:
        super().scrape(driver)

    def _extract_data(self, driver: _WebDriver):
        article_list_dom = driver.find_element(By.XPATH, _Parameters.ARTICLE_LIST_XPATH.value)
        articles_dom = article_list_dom.find_elements(By.XPATH, _Parameters.ARTICLES_XPATH.value)

        article_list = []
        for article_dom in articles_dom:
            article_title_dom = article_dom.find_element(By.XPATH, _Parameters.ARTICLE_TITLE_XPATH.value)
            title = article_title_dom.text
            href = article_title_dom.get_attribute("href")

            article_list.append(OpenNewsArticle(title=title, url=href))

        self._article_list = article_list
