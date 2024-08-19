from pages.main_page import MainPage
from pages.order_page import OrderPage
from settings import Url, Data, MainData


class TestsOrdersScooters:
    def test_order_main_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Url.QA_SCOOTER_SERVICE)
        main_page.click_on_the_main_order_button()
        order_page = OrderPage(driver)
        order_page.set_name_field(Data.name_second)
        order_page.set_surname_fild(Data.surname_second)
        order_page.set_adress_fild(Data.adresse_second)
        order_page.set_subway_fild_sokol(Data.subway_second)
        order_page.set_phone_fild(Data.phone_second)
        order_page.click_button_next()
        order_page.set_when_to_bring_the_scooter(Data.date_second)
        order_page.set_two_day_period()
        order_page.set_grey_color()
        order_page.set_comment(Data.comment_second)
        order_page.click_button_order()
        order_page.click_confirmation_button()
        order = OrderPage(driver)
        assert order.get_success_popup().is_displayed()


    def test_order_header_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Url.QA_SCOOTER_SERVICE)
        main_page.click_on_the_header_order_button()
        order_page = OrderPage(driver)
        order_page.set_name_field(Data.name)
        order_page.set_surname_fild(Data.surname)
        order_page.set_adress_fild(Data.adresse)
        order_page.set_subway_fild(Data.subway)
        order_page.set_phone_fild(Data.phone)
        order_page.click_button_next()
        order_page.set_when_to_bring_the_scooter(Data.date)
        order_page.set_one_day_period()
        order_page.set_black_color()
        order_page.set_comment(Data.comment)
        order_page.click_button_order()
        order_page.click_confirmation_button()
        order = OrderPage(driver)
        assert order.get_success_popup().is_displayed()

    def test_to_redirect_to_the_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Url.QA_SCOOTER_SERVICE)
        main_page.click_on_the_header_order_button()
        order_page = OrderPage(driver)
        order_page.set_name_field(Data.name)
        order_page.click_on_the_logo_scooter()
        current_url = OrderPage(driver)
        assert current_url.get_current_url() == Url.QA_SCOOTER_SERVICE








