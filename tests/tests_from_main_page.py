from pages.main_page import MainPage

class TestFromMainPage:
    def test_redirect_to_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_the_yandex_logo()
        dzen_page = MainPage(driver)

        assert dzen_page.get_dzen_popup().is_displayed()
