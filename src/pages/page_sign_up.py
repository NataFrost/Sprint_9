from src.pages.page_base import BasePage
from src.locators.sign_up_locators import SignUpLocators
from src.data.constants import Labels


class SignUpPage(BasePage):

    def open_sign_up_page(self):
        self.click_element(SignUpLocators.SIGN_UP_HEADER, Labels.SIGN_UP_HEADER)

    def enter_name(self, name):
        self.fill_input_field(SignUpLocators.NAME, Labels.SIGN_UP_NAME, name)

    def enter_surname(self, surname):
        self.fill_input_field(SignUpLocators.SURNAME, Labels.SIGN_UP_SURNAME, surname)

    def enter_username(self, username):
        self.fill_input_field(SignUpLocators.USERNAME, Labels.SIGN_UP_USERNAME, username)

    def enter_email(self, email):
        self.fill_input_field(SignUpLocators.EMAIL, Labels.SIGN_UP_EMAIL, email)

    def enter_password(self, password):
        self.fill_input_field(SignUpLocators.PASSWORD, Labels.SIGN_UP_PASSWORD, password)

    def submit_button_click(self):
        self.click_element(SignUpLocators.SIGN_UP_BUTTON, Labels.SIGN_UP_BUTTON)
