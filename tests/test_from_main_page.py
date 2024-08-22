import allure
import pytest
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from settings import Url, MainData


class TestFromMainPage:
    @allure.title('Проверка редиректа на дзен при клике на иконку Яндекса')
    def test_redirect_to_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Url.QA_SCOOTER_SERVICE)
        main_page.click_on_the_yandex_logo()
        dzen_page = MainPage(driver)
        dzen_page.wait_dzen_page_element()
        assert dzen_page.get_dzen_popup().is_displayed()

    @allure.title('Проверка блока вопрос-ответ')
    @pytest.mark.parametrize('accordion_question, accordion_answer, answer_text',
                             [[MainPageLocators.ACCORDION_QUESTION_1, MainPageLocators.ACCORDION_ANSWER_1, MainData.ANSWER_TEXT],
                              [MainPageLocators.ACCORDION_QUESTION_2, MainPageLocators.ACCORDION_ANSWER_2, MainData.ANSWER_TEXT_SECOND],
                              [MainPageLocators.ACCORDION_QUESTION_3, MainPageLocators.ACCORDION_ANSWER_3, MainData.ANSWER_TEXT_THIRD],
                             [MainPageLocators.ACCORDION_QUESTION_4, MainPageLocators.ACCORDION_ANSWER_4, MainData.ANSWER_TEXT_FOURTH],
                             [MainPageLocators.ACCORDION_QUESTION_5, MainPageLocators.ACCORDION_ANSWER_5, MainData.ANSWER_TEXT_FIFTH],
                             [MainPageLocators.ACCORDION_QUESTION_6, MainPageLocators.ACCORDION_ANSWER_6, MainData.ANSWER_TEXT_SIXTH],
                             [MainPageLocators.ACCORDION_QUESTION_7, MainPageLocators.ACCORDION_ANSWER_7, MainData.ANSWER_TEXT_SEVENTH],
                             [MainPageLocators.ACCORDION_QUESTION_8, MainPageLocators.ACCORDION_ANSWER_8, MainData.ANSWER_TEXT_EIGHTH]])
    def test_get_answer(self, accordion_question, accordion_answer, answer_text, driver):
        question = MainPage(driver)
        question.open_page(Url.QA_SCOOTER_SERVICE)
        question.click_on_the_questions_button(accordion_question)
        question.wait_and_find_element(accordion_answer)
        assert question.get_answer(accordion_answer, answer_text) == answer_text









