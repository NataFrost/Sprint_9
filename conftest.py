import tempfile

import pytest
from selenium import webdriver
from src.config import URL

from src.pages.page_sign_up import SignUpPage
from src.pages.page_sign_in import SignInPage
from src.helpers import get_sign_up_data
from src.data.data import TestData


def browser_settings():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless=new')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument(f'--user-data-dir={tempfile.mkdtemp()}')
    # chrome_options.add_argument(f'--window-size={RESOLUTION[0]},{RESOLUTION[1]}')
    return chrome_options


@pytest.fixture
def driver():
    chrome = webdriver.Chrome(options=browser_settings())
    chrome.get(URL)
    chrome.maximize_window()
    yield chrome
    chrome.quit()


# создать пользователя
@pytest.fixture
def user(driver):
    username, email, password = get_sign_up_data()
    page = SignUpPage(driver)
    page.open_sign_up_page()
    page.enter_name(TestData.USER_NAME)
    page.enter_surname(TestData.USER_SURNAME)
    page.enter_username(username)
    page.enter_email(email)
    page.enter_password(password)
    page.submit_button_click()
    yield email, password


# создать пользователя и залогиниться
@pytest.fixture
def login_new_user(driver, user):
    email, password = user
    page = SignInPage(driver)
    page.open_sign_in_page()
    page.enter_email(email)
    page.enter_password(password)
    page.submit_button_click()


# если нужно, то можно использовать какого-то существующего пользователя
@pytest.fixture
def login(driver):
    email, password = TestData.USER_EMAIL, TestData.USER_PASSWORD
    page = SignInPage(driver)
    page.open_sign_in_page()
    page.enter_email(email)
    page.enter_password(password)
    page.submit_button_click()
