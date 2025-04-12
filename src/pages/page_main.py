import allure
from src.pages.page_base import BasePage
from src.locators.sign_up_locators import SignUpLocators


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Проверка, что отображается кнопка 'Выход'")
    def logout_button_is_displayed(self):
        logout_button = self.find_element(SignUpLocators.LOGOUT_HEADER)
        return logout_button.is_displayed()
