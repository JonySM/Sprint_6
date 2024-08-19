from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_FILD = (By.XPATH, ".//input[@placeholder ='* Имя']")  # Имя
    SURNAME_FILD = (By.XPATH, ".//input[@placeholder ='* Фамилия']")  # Фамилия
    ADRESS_FILD = (By.XPATH, ".//input[@placeholder ='* Адрес: куда привезти заказ']")  # Адрес
    SUBWAY_FILD = (By.XPATH, ".//input[@placeholder ='* Станция метро']")  # Метро
    SUBWAY_DROP_VOIK = (By.XPATH, ".//div[text()='Войковская']")  # Войковская
    SUBWAY_DROP_SOKOL = (By.XPATH, ".//div[text()='Сокол']")  # Сокол
    PHONE_FILD = (By.XPATH, ".//input[@placeholder ='* Телефон: на него позвонит курьер']")  # Телефон
    DATA_FILD = (By.XPATH, ".//input[@placeholder ='* Когда привезти самокат']")  # Дата выдачи самоката
    PERIOD_FILD = (By.XPATH, ".//span[@class ='Dropdown-arrow']")  # Срок аренды
    BLACK_COLOR_SCOOTER_BOX = (By.XPATH, ".//input[@id='black']")  # Чекбокс черный
    GREY_COLOR_SCOOTER_BOX = (By.XPATH, ".//input[@id='grey']")  # Чекбокс серый
    COMMENT_FILD = (By.XPATH, ".//input[@placeholder = 'Комментарий для курьера']")  # Коммент для курьера
    NEXT_BUTTON = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")  # Кнопка далее
    ORDER_BUTTON = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")  # Кнопка заказать
    CONFIRMATION_ORDER_BUTTON = (By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[text()='Да']")  # Кнопка да
    ONE_DAY = (By.XPATH, ".//div[text()='сутки']")  # Дропдаун на одни сутки
    TWO_DAY = (By.XPATH, ".//div[text()='двое суток']")  # Дропдаун на двое суток
    SUCCESS_ORDER_POPUP = (By.XPATH, ".//div[@class='Order_ModalHeader__3FDaJ']")  # Попап успешного заказа
    LOGO_SCOOTER =(By.XPATH, ".//a[@class='Header_LogoScooter__3lsAR']")  # Логотип самокат



