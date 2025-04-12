import allure

from src.pages.page_base import BasePage
from src.locators.create_recipe_locators import CreateRecipeLocators
from src.data.data import TestData
from src.data.constants import Labels


class PageCreateRecipe(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open_create_recipe_page(self):
        self.click_element(CreateRecipeLocators.CREATE_RECIPE_HEADER, Labels.CREATE_RECIPE_HEADER)

    def enter_receipt_name(self, name):
        self.fill_input_field(CreateRecipeLocators.RECIPE_NAME_INPUT, Labels.RECIPE_NAME, name)

    @allure.step('Загрузить фотографию')
    def upload_photo(self, photo):
        self.scroll_to_element(CreateRecipeLocators.BUTTON_CREATE_RECIPE)
        self.make_element_visible(CreateRecipeLocators.INPUT_FILE)
        self.load_file(CreateRecipeLocators.INPUT_FILE, str(photo))

    @allure.step('Выбрать первый ингредиент из списка по первой букве')
    def select_ingredient(self, ingredient):
        self.fill_input_field(CreateRecipeLocators.INGREDIENT_INPUT, Labels.INGREDIENTS, ingredient[0])
        self.wait_element_located(CreateRecipeLocators.INGREDIENTS_DROPDOWN)
        ingredients = self.find_elements(CreateRecipeLocators.INGREDIENTS_DROPDOWN_LIST)
        ingredients[0].click()

    def enter_weight(self, weight):
        self.fill_input_field(CreateRecipeLocators.AMOUNT_INPUT, Labels.AMOUNT, weight)

    def add_ingredient(self):
        self.click_element(CreateRecipeLocators.INGREDIENT_ADD_LINK, Labels.ADD_INGREDIENT)

    def enter_cooking_time(self, time):
        self.fill_input_field(CreateRecipeLocators.TIME_INPUT, Labels.COOKING_TIME, time)

    def enter_recipe_description(self, text):
        self.fill_input_field(CreateRecipeLocators.RECIPE_DESCRIPTION_INPUT, Labels.RECIPE_DESCRIPTION, text)

    def create_recipe(self):
        self.click_element(CreateRecipeLocators.BUTTON_CREATE_RECIPE, Labels.CREATE_RECIPE_BUTTON)


