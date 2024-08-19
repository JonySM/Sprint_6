from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_ORDER_BUTTON = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")  # Кнопка заказать  в середине страницы
    HEADER_ORDER_BUTTON = (By.XPATH, ".//button[@class = 'Button_Button__ra12g']")  # Кнопка заказа в заголовке страницы
    DZEN = (By.XPATH, ".//div[@class='m4275241c']")  # Попап яндекс
    YANDEX_LOGO = (By.XPATH, ".//a[@class='Header_LogoYandex__3TSOI']")  # Яндекс лого
    ACCORDION_QUESTION_1 = (By.XPATH, ".//div[@aria-controls= 'accordion__panel-0']")  # Первый вопрос
    ACCORDION_ANSWER_1 = (By.XPATH, ".//div[@id='accordion__panel-0']")  # Ответ на первый вопрос
    ACCORDION_QUESTION_2 = (By.XPATH, ".//div[@aria-controls= 'accordion__panel-1']")  # Второй вопрос
    ACCORDION_ANSWER_2 = (By.XPATH, ".//div[@id='accordion__panel-1']")  # Ответ на второй вопрос
    ACCORDION_QUESTION_3 = (By.XPATH, ".//div[@aria-controls= 'accordion__panel-2']")  # Третий вопрос
    ACCORDION_ANSWER_3 = (By.XPATH, ".//div[@id='accordion__panel-2']")  # Ответ на третий вопрос
    ACCORDION_QUESTION_4 = (By.XPATH, ".//div[@aria-controls= 'accordion__panel-3']")  # Четвертый вопрос
    ACCORDION_ANSWER_4 = (By.XPATH, ".//div[@id='accordion__panel-3']")  # Ответ на четвертый вопрос
    ACCORDION_QUESTION_5 = (By.XPATH, ".//div[@aria-controls= 'accordion__panel-4']")  # Пятый вопрос
    ACCORDION_ANSWER_5 = (By.XPATH, ".//div[@id='accordion__panel-4']")  # Ответ на пятый вопрос
    ACCORDION_QUESTION_6 = (By.XPATH, ".//div[@aria-controls= 'accordion__panel-5']")  # Шестой вопрос
    ACCORDION_ANSWER_6 = (By.XPATH, ".//div[@id='accordion__panel-5']")  # Ответ на шестой вопрос
    ACCORDION_QUESTION_7 = (By.XPATH, ".//div[@aria-controls= 'accordion__panel-6']")  # Седьмой вопрос
    ACCORDION_ANSWER_7 = (By.XPATH, ".//div[@id='accordion__panel-6']")  # Ответ на седьмой вопрос
    ACCORDION_QUESTION_8 = (By.XPATH, ".//div[@aria-controls= 'accordion__panel-7']")  # Восьмой вопрос
    ACCORDION_ANSWER_8 = (By.XPATH, ".//div[@id='accordion__panel-7']")  # Ответ на восьмой вопрос


