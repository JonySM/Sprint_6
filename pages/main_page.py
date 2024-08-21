from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def click_on_the_questions_button(self, locator):
        question_button = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", question_button)

    def get_answer(self, locator, text):
        current_text = self.wait_text_and_find_element(locator, text)
        return current_text.text

    def click_on_the_main_order_button(self):
        main_order_button = self.driver.find_element(*MainPageLocators.MAIN_ORDER_BUTTON)
        self.driver.execute_script("arguments[0].click();", main_order_button)

    def click_on_the_header_order_button(self):
        header_order_button = self.wait_and_find_element(MainPageLocators.HEADER_ORDER_BUTTON)
        header_order_button.click()

    def click_on_the_yandex_logo(self):
        yandex_logo = self.wait_and_find_element(MainPageLocators.YANDEX_LOGO)
        yandex_logo.click()

    def get_dzen_popup(self):
        dzen_popup = self.wait_and_find_element(MainPageLocators.DZEN)
        return dzen_popup










