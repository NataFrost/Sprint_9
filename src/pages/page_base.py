import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                          message=f"Element not found: {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                          message=f"Elements not found: {locator}")

    @allure.step("Нажать на элемент {field_name}")
    def click_element(self, locator, field_name='Placeholder', time=10):
        WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Заполнить поле {field_name} значением {value}")
    def fill_input_field(self, locator, field_name, value):
        input_field = self.find_element(locator)
        input_field.clear()
        input_field.click()
        input_field.send_keys(value)

    @allure.step("Открыт URL: {url}")
    def wait_url(self, url, time=10):
        return WebDriverWait(self.driver, time).until(EC.url_to_be(url))

    @allure.step("Проверить текущий URL")
    def check_url(self):
        return self.driver.current_url

    @allure.step("Открыть URL: {url}")
    def go_to_url(self, url):
        self.driver.get(url)

    def wait_element_located(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))

    def wait_element_to_be_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    def wait_text_in_element(self, locator, value):
        return WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(locator, value))

    def wait_text_not_in_element(self, locator, value):
        WebDriverWait(self.driver, 10).until_not(
            EC.text_to_be_present_in_element(locator, value)
        )

    def wait_non_empty_text_in_element(self, locator):
        """Ждёт, пока элемент не будет содержать непустой текст."""
        return WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*locator).text.strip() != ""
        )

    def make_element_visible(self, locator):
        file_input = self.find_element(locator)
        self.driver.execute_script("arguments[0].style.display = 'block';", file_input)

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def load_file(self, locator, file_location):
        element = self.find_element(locator)
        element.send_keys(file_location)
