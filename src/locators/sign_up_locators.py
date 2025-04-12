from selenium.webdriver.common.by import By


class SignUpLocators:

    SIGN_UP_HEADER = (By.XPATH, ".//a[@href='/signup']")
    NAME = (By.XPATH, ".//input[@name='first_name']")
    SURNAME = (By.XPATH, ".//input[@name='last_name']")
    USERNAME = (By.XPATH, ".//input[@name='username']")
    EMAIL = (By.XPATH, ".//input[@name='email']")
    PASSWORD = (By.XPATH, ".//input[@name='password']")
    SIGN_UP_BUTTON = (By.XPATH, ".//form/button")

    LOGOUT_HEADER = (By.XPATH, ".//a[text()='Выход']")
