from src.pages.page_base import BasePage

from src.locators.sign_in_locators import SignInLocators
from src.data.constants import Labels


class SignInPage(BasePage):

    def open_sign_in_page(self):
        self.click_element(SignInLocators.SIGN_IN_HEADER, Labels.SIGN_IN_HEADER)

    def enter_email(self, email):
        self.fill_input_field(SignInLocators.EMAIL, Labels.SIGN_IN_EMAIL, email)

    def enter_password(self, password):
        self.fill_input_field(SignInLocators.PASSWORD, Labels.SIGN_IN_PASSWORD, password)

    def submit_button_click(self):
        self.click_element(SignInLocators.SIGN_IN_BUTTON, Labels.SIGN_IN_BUTTON)

    def get_page_title(self):
        self.wait_text_in_element(SignInLocators.SIGN_IN_TITLE, Labels.SIGN_IN_TITLE)
        return self.find_element(SignInLocators.SIGN_IN_TITLE).text
