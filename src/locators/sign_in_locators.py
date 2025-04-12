from selenium.webdriver.common.by import By


class SignInLocators:

    SIGN_IN_HEADER = (By.XPATH, ".//a[@href='/signin']")
    EMAIL = (By.XPATH, ".//input[@name='email']")
    PASSWORD = (By.XPATH, ".//input[@name='password']")
    SIGN_IN_BUTTON = (By.XPATH, ".//form/button")
    SIGN_IN_TITLE = (By.XPATH, ".//h1")
