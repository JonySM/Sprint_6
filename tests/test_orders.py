import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from settings import Url, Data


class TestsOrdersScooters:
    @allure.title('Проверка создания заказа с главной кнопки')
    @allure.description('Клик на основную кнопку заказа и проверка заполнения формы и оформления заказа')
    def test_order_main_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Url.QA_SCOOTER_SERVICE)
        main_page.click_on_the_main_order_button()
        order_page = OrderPage(driver)
        order_page.set_name_field(Data.NAME_SECOND)
        order_page.set_surname_fild(Data.SURNAME_SECOND)
        order_page.set_address_fild(Data.ADDRESS_SECOND)
        order_page.set_subway_fild_sokol(Data.SUBWAY_SECOND)
        order_page.set_phone_fild(Data.PHONE_SECOND)
        order_page.click_button_next()
        order_page.set_when_to_bring_the_scooter(Data.DATE_SECOND)
        order_page.set_two_day_period()
        order_page.set_grey_color()
        order_page.set_comment(Data.COMMENT_SECOND)
        order_page.click_button_order()
        order_page.click_confirmation_button()
        order = OrderPage(driver)
        assert order.get_success_popup().is_displayed()

    @allure.title('Проверка создания заказа с  кнопки в шапке')
    @allure.description('Клик на  кнопку заказа в шапке страницы и проверка заполнения формы и оформления заказа')
    def test_order_header_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Url.QA_SCOOTER_SERVICE)
        main_page.click_on_the_header_order_button()
        order_page = OrderPage(driver)
        order_page.set_name_field(Data.NAME)
        order_page.set_surname_fild(Data.SURNAME)
        order_page.set_address_fild(Data.ADDRESS)
        order_page.set_subway_fild(Data.SUBWAY)
        order_page.set_phone_fild(Data.PHONE)
        order_page.click_button_next()
        order_page.set_when_to_bring_the_scooter(Data.DATE)
        order_page.set_one_day_period()
        order_page.set_black_color()
        order_page.set_comment(Data.COMMENT)
        order_page.click_button_order()
        order_page.click_confirmation_button()
        order = OrderPage(driver)
        assert order.get_success_popup().is_displayed()

    @allure.title('Проверка редирект на главную страницу при клике на иконку самокат')
    def test_to_redirect_to_the_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Url.QA_SCOOTER_SERVICE)
        main_page.click_on_the_header_order_button()
        order_page = OrderPage(driver)
        order_page.set_name_field(Data.NAME)
        order_page.click_on_the_logo_scooter()
        current_url = OrderPage(driver)
        assert current_url.get_current_url() == Url.QA_SCOOTER_SERVICE

    @pytest.mark.parametrize('name', ['Evgeniy', 'Евгений24', 'Евгенийййййййййй', '12345'])
    def test_set_name_field(self, name, driver):
        main_page = MainPage(driver)
        main_page.open_page(Url.QA_SCOOTER_SERVICE)
        main_page.click_on_the_header_order_button()
        order_page = OrderPage(driver)
        order_page.set_name_field(name)
        order_page.set_surname_fild(Data.SURNAME)
        error_message = OrderPage(driver)
        assert error_message.get_error_message_name().is_displayed()

    @pytest.mark.parametrize('surname', ['Evgenyev', 'Евгеньев24', '12345'])
    def test_set_surname_fild(self, surname, driver):
        main_page = MainPage(driver)
        main_page.open_page(Url.QA_SCOOTER_SERVICE)
        main_page.click_on_the_header_order_button()
        order_page = OrderPage(driver)
        order_page.set_name_field(Data.NAME)
        order_page.set_surname_fild(surname)
        order_page.set_address_fild(Data.ADDRESS)
        error_message = OrderPage(driver)
        assert error_message.get_error_message_surname().is_displayed()

    @pytest.mark.parametrize('address', ['Moscow', 'М', '1234'])
    def test_set_address_fild(self, address, driver):
        main_page = MainPage(driver)
        main_page.open_page(Url.QA_SCOOTER_SERVICE)
        main_page.click_on_the_header_order_button()
        order_page = OrderPage(driver)
        order_page.set_name_field(Data.NAME)
        order_page.set_surname_fild(Data.SURNAME)
        order_page.set_address_fild(address)
        order_page.set_subway_fild(Data.SUBWAY)
        error_message = OrderPage(driver)
        assert error_message.get_error_message_address().is_displayed()

    @pytest.mark.parametrize('phone', ['Телефон', 'Phone', '7915545554', '79155456655224'])
    def test_set_phone_fild(self, phone, driver):
        main_page = MainPage(driver)
        main_page.open_page(Url.QA_SCOOTER_SERVICE)
        main_page.click_on_the_header_order_button()
        order_page = OrderPage(driver)
        order_page.set_name_field(Data.NAME)
        order_page.set_surname_fild(Data.SURNAME)
        order_page.set_address_fild(Data.ADDRESS)
        order_page.set_subway_fild(Data.SUBWAY)
        order_page.set_phone_fild(phone)
        order_page.click_button_next()
        error_message = OrderPage(driver)
        assert error_message.get_error_message_phone().is_displayed()

















