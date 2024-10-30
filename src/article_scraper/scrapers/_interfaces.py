import abc as _abc

from selenium.webdriver.remote.webdriver import WebDriver as _WebDriver


class ArticleInterface(_abc.ABC):

    @_abc.abstractmethod
    def retrieve_content(self) -> None:
        pass


class NewsScraperInterface(_abc.ABC):
    
    @_abc.abstractmethod
    def scrape(self, driver: _WebDriver | None = None) -> None:
        pass

    @_abc.abstractmethod
    def retrieve_articles(self) -> None:
        pass
