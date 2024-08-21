import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Заполняем поле имя')
    def set_name_field(self, name):
        name_fild = self.wait_and_find_element(OrderPageLocators.NAME_FILD)
        name_fild.send_keys(name)

    @allure.step('Заполняем поле фамилия')
    def set_surname_fild(self, surname):
        surname_fild = self.wait_and_find_element(OrderPageLocators.SURNAME_FILD)
        surname_fild.send_keys(surname)

    @allure.step('Заполняем поле адрес')
    def set_address_fild(self, adress):
        adress_fild = self.wait_and_find_element(OrderPageLocators.ADDRESS_FILD)
        adress_fild.send_keys(adress)

    @allure.step('Заполняем поле метро станцией "Войковская"')
    def set_subway_fild(self, subway):
        subway_fild = self.wait_and_find_element(OrderPageLocators.SUBWAY_FILD)
        subway_fild.send_keys(subway)
        subway_drop_station = self.wait_and_find_element(OrderPageLocators.SUBWAY_DROP_VOIK)
        subway_drop_station.click()

    @allure.step('Заполняем поле метро станцией "Сокол"')
    def set_subway_fild_sokol(self, subway):
        subway_fild_sokol = self.wait_and_find_element(OrderPageLocators.SUBWAY_FILD)
        subway_fild_sokol.send_keys(subway)
        subway_drop_station_sokol = self.wait_and_find_element(OrderPageLocators.SUBWAY_DROP_SOKOL)
        subway_drop_station_sokol.click()

    @allure.step('Заполняем поле телефон')
    def set_phone_fild (self, phone):
        phone_fild = self.wait_and_find_element(OrderPageLocators.PHONE_FILD)
        phone_fild.send_keys(phone)

    @allure.step('Кликаем кнопку далее')
    def click_button_next(self):
        next_button = self.wait_and_find_element(OrderPageLocators.NEXT_BUTTON)
        next_button.click()

    @allure.step('Кликаем кнопку "Заказать"')
    def click_button_order(self):
        order_button = self.wait_and_find_element(OrderPageLocators.ORDER_BUTTON)
        order_button.click()

    @allure.step('Кликаем кнопку "Да" в попап заказа')
    def click_confirmation_button(self):
        confirmation_button = self.wait_and_find_element(OrderPageLocators.CONFIRMATION_ORDER_BUTTON)
        confirmation_button.click()

    @allure.step('Заполняем дату выдачи самоката')
    def set_when_to_bring_the_scooter(self, data):
        data_fild = self.wait_and_find_element(OrderPageLocators.DATA_FILD)
        data_fild.send_keys(data)

    @allure.step('Выбираем срок аренды "Сутки"')
    def set_one_day_period(self):
        period_fild = self.wait_and_find_element(OrderPageLocators.PERIOD_FILD)
        period_fild.click()
        day = self.wait_and_find_element(OrderPageLocators.ONE_DAY)
        day.click()

    @allure.step('Выбираем срок аренды "Двое суток"')
    def set_two_day_period(self):
        period_fild = self.wait_and_find_element(OrderPageLocators.PERIOD_FILD)
        period_fild.click()
        two_day = self.wait_and_find_element(OrderPageLocators.TWO_DAY)
        two_day.click()

    @allure.step('Выбираем цвет самоката "Черный жемчуг"')
    def set_black_color(self):
        black_color = self.wait_and_find_element(OrderPageLocators.BLACK_COLOR_SCOOTER_BOX)
        black_color.click()

    @allure.step('Выбираем цвет самоката "Серая безысходность"')
    def set_grey_color(self):
        grey_color = self.wait_and_find_element(OrderPageLocators.GREY_COLOR_SCOOTER_BOX)
        grey_color.click()

    @allure.step('Заполняем комментарий"')
    def set_comment(self, comment):
        comment_fild = self.wait_and_find_element(OrderPageLocators.COMMENT_FILD)
        comment_fild.send_keys(comment)

    @allure.step('Получаем успешный попап на странице заказа')
    def get_success_popup(self):
        success_popup = self.wait_and_find_element(OrderPageLocators.SUCCESS_ORDER_POPUP)
        return success_popup

    @allure.step('Клик на логотип самоката')
    def click_on_the_logo_scooter(self):
        logo_scooter = self.wait_and_find_element(OrderPageLocators.LOGO_SCOOTER)
        logo_scooter.click()

    @allure.step('Получаем тултип ошибки заполнения поля имя')
    def get_error_message_name(self):
        error_message_name = self.wait_and_find_element(OrderPageLocators.ERROR_MESSAGE_NAME)
        return error_message_name

    @allure.step('Получаем тултип ошибки заполнения поля фамилия')
    def get_error_message_surname(self):
        error_message_surname = self.wait_and_find_element(OrderPageLocators.ERROR_MESSAGE_SURNAME)
        return error_message_surname

    @allure.step('Получаем тултип ошибки заполнения поля адрес')
    def get_error_message_address(self):
        error_message_address = self.wait_and_find_element(OrderPageLocators.ERROR_MESSAGE_ADDRESS)
        return error_message_address

    @allure.step('Получаем тултип ошибки заполнения поля телефон')
    def get_error_message_phone(self):
        error_message_phone = self.wait_and_find_element(OrderPageLocators.ERROR_MESSAGE_PHONE)
        return error_message_phone













