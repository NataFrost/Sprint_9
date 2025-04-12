from src.pages.page_sign_in import SignInPage
from src.pages.page_main import MainPage


class TestSignIn:

    def test_sign_in(self, driver, user):
        email, password = user
        page = SignInPage(driver)
        page.open_sign_in_page()
        page.enter_email(email)
        page.enter_password(password)
        page.submit_button_click()
        main_page = MainPage(driver)
        assert main_page.logout_button_is_displayed()
