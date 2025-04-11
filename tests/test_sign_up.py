import allure

from src.helpers import get_sign_up_data, allure_attach
from src.data.data import TestData
from src.data.constants import Labels

from src.pages.page_sign_up import SignUpPage
from src.pages.page_sign_in import SignInPage


class TestSignUp:

    def test_sign_up(self, driver):
        username, email, password = get_sign_up_data()
        page = SignUpPage(driver)
        page.open_sign_up_page()
        page.enter_name(TestData.USER_NAME)
        page.enter_surname(TestData.USER_SURNAME)
        page.enter_username(username)
        page.enter_email(email)
        page.enter_password(password)
        page.submit_button_click()

        page_sign_in = SignInPage(driver)
        with allure.step("Проверка, что открылась сраница авторизации"):
            assert page_sign_in.get_page_title() == Labels.SIGN_IN_TITLE
            allure_attach(page_sign_in.get_page_title(), Labels.SIGN_IN_TITLE, "Заголовок страницы")
