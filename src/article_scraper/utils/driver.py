from selenium import webdriver as _webdriver
from selenium.webdriver.firefox.options import Options as _FirefoxOptions


def get_driver() -> _webdriver.Firefox:
    driver_options = _FirefoxOptions()
    driver_options.add_argument("--headless")
    
    driver = _webdriver.Firefox(options=driver_options)

    return driver
