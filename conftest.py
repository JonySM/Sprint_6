import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from settings import Url


@pytest.fixture(scope='function')
def driver():
    firefox_driver = webdriver.Firefox(service=FirefoxService(
    r'C:\Users\e.sergeev\WebDriver\bin\geckodriver.exe'))
    firefox_driver.maximize_window()
    firefox_driver.get(Url.QA_SCOOTER_SERVICE)
    yield firefox_driver
    firefox_driver.quit()



