from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from settings import MainData, Url


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_and_find_element(self, locator) -> WebElement:
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_find_and_click_element(self, locator) -> WebElement:
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_text_and_find_element(self, locator, text) -> WebElement:
        WebDriverWait(self.driver, 30).until(expected_conditions.text_to_be_present_in_element(locator, text))
        return self.driver.find_element(*locator)

    def wait_current_url(self, url):
        current_url = WebDriverWait(self.driver, 30).until(expected_conditions.url_to_be(url))
        return current_url

    def open_page(self, url):
        self.driver.get(url)

    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

