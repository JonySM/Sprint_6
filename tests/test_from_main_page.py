import allure
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

    @allure.title('Проверка текста в форме вопрос-ответ. Вопрос 1')
    def test_get_first_answer(self, driver):
        question = MainPage(driver)
        question.open_page(Url.QA_SCOOTER_SERVICE)
        question.click_on_the_questions_button(MainPageLocators.ACCORDION_QUESTION_1)
        answer = MainPage(driver)
        answer.wait_and_find_element(MainPageLocators.ACCORDION_ANSWER_1)
        assert answer.get_answer(MainPageLocators.ACCORDION_ANSWER_1,
                                     MainData.ANSWER_TEXT) == MainData.ANSWER_TEXT

    @allure.title('Проверка текста в форме вопрос-ответ. Вопрос 2')
    def test_get_second_answer(self, driver):
        question = MainPage(driver)
        question.open_page(Url.QA_SCOOTER_SERVICE)
        question.click_on_the_questions_button(MainPageLocators.ACCORDION_QUESTION_2)
        answer = MainPage(driver)
        answer.wait_and_find_element(MainPageLocators.ACCORDION_ANSWER_2)
        assert answer.get_answer(MainPageLocators.ACCORDION_ANSWER_2,
                                     MainData.ANSWER_TEXT_SECOND) == MainData.ANSWER_TEXT_SECOND

    @allure.title('Проверка текста в форме вопрос-ответ. Вопрос 3')
    def test_get_third_answer(self, driver):
        question = MainPage(driver)
        question.open_page(Url.QA_SCOOTER_SERVICE)
        question.click_on_the_questions_button(MainPageLocators.ACCORDION_QUESTION_3)
        answer = MainPage(driver)
        answer.wait_and_find_element(MainPageLocators.ACCORDION_ANSWER_3)
        assert answer.get_answer(MainPageLocators.ACCORDION_ANSWER_3,
                                     MainData.ANSWER_TEXT_THIRD) == MainData.ANSWER_TEXT_THIRD

    @allure.title('Проверка текста в форме вопрос-ответ. Вопрос 4')
    def test_get_fourth_answer(self, driver):
        question = MainPage(driver)
        question.open_page(Url.QA_SCOOTER_SERVICE)
        question.click_on_the_questions_button(MainPageLocators.ACCORDION_QUESTION_4)
        answer = MainPage(driver)
        answer.wait_and_find_element(MainPageLocators.ACCORDION_ANSWER_4)
        assert answer.get_answer(MainPageLocators.ACCORDION_ANSWER_4,
                                     MainData.ANSWER_TEXT_FOURTH) == MainData.ANSWER_TEXT_FOURTH

    @allure.title('Проверка текста в форме вопрос-ответ. Вопрос 5')
    def test_get_fifth_answer(self, driver):
        question = MainPage(driver)
        question.open_page(Url.QA_SCOOTER_SERVICE)
        question.click_on_the_questions_button(MainPageLocators.ACCORDION_QUESTION_5)
        answer = MainPage(driver)
        answer.wait_and_find_element(MainPageLocators.ACCORDION_ANSWER_5)
        assert answer.get_answer(MainPageLocators.ACCORDION_ANSWER_5,
                                     MainData.ANSWER_TEXT_FIFTH) == MainData.ANSWER_TEXT_FIFTH

    @allure.title('Проверка текста в форме вопрос-ответ. Вопрос 6')
    def test_get_sixth_answer(self, driver):
        question = MainPage(driver)
        question.open_page(Url.QA_SCOOTER_SERVICE)
        question.click_on_the_questions_button(MainPageLocators.ACCORDION_QUESTION_6)
        answer = MainPage(driver)
        answer.wait_and_find_element(MainPageLocators.ACCORDION_ANSWER_6)
        assert answer.get_answer(MainPageLocators.ACCORDION_ANSWER_6,
                                     MainData.ANSWER_TEXT_SIXTH) == MainData.ANSWER_TEXT_SIXTH

    @allure.title('Проверка текста в форме вопрос-ответ. Вопрос 7')
    def test_get_seventh_answer(self, driver):
        question = MainPage(driver)
        question.open_page(Url.QA_SCOOTER_SERVICE)
        question.click_on_the_questions_button(MainPageLocators.ACCORDION_QUESTION_7)
        answer = MainPage(driver)
        answer.wait_and_find_element(MainPageLocators.ACCORDION_ANSWER_7)
        assert answer.get_answer(MainPageLocators.ACCORDION_ANSWER_7,
                                     MainData.ANSWER_TEXT_SEVENTH) == MainData.ANSWER_TEXT_SEVENTH

    @allure.title('Проверка текста в форме вопрос-ответ. Вопрос 8')
    def test_get_eight_answer(self, driver):
        question = MainPage(driver)
        question.open_page(Url.QA_SCOOTER_SERVICE)
        question.click_on_the_questions_button(MainPageLocators.ACCORDION_QUESTION_8)
        answer = MainPage(driver)
        answer.wait_and_find_element(MainPageLocators.ACCORDION_ANSWER_8)
        assert answer.get_answer(MainPageLocators.ACCORDION_ANSWER_8,
                                     MainData.ANSWER_TEXT_EIGHTH) == MainData.ANSWER_TEXT_EIGHTH
