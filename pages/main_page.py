import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Клик на стрелку вопроса, раздела "Вопрос ответ"')
    def click_on_the_questions_button(self, locator):
        super().find_and_click_element(locator)

    @allure.step('Клик на кнопку "Заказать" в середине страницы')
    def click_on_the_main_order_button(self):
        self.find_and_click_element(MainPageLocators.MAIN_ORDER_BUTTON)

    @allure.step('Получаем ответ на вопрос')
    def get_answer(self, locator, text):
        current_text = self.wait_text_and_find_element(locator, text)
        return current_text.text

    @allure.step('Клик на кнопку "Заказать" в шапке страницы')
    def click_on_the_header_order_button(self):
        header_order_button = self.wait_and_find_element(MainPageLocators.HEADER_ORDER_BUTTON)
        header_order_button.click()

    @allure.step('Клик на логотип Яндекс в шапке страницы')
    def click_on_the_yandex_logo(self):
        yandex_logo = self.wait_and_find_element(MainPageLocators.YANDEX_LOGO)
        yandex_logo.click()

    @allure.step('Получаем попап на странице Dzen.ru')
    def get_dzen_popup(self):
        dzen_popup = self.wait_and_find_element(MainPageLocators.DZEN)
        return dzen_popup










