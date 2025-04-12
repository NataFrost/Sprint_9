from src.pages.page_base import BasePage
from src.locators.recipe_locators import RecipeLocators


class RecipePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_recipe_name(self):
        self.wait_text_not_in_element(RecipeLocators.RECIPE_NAME, "Создание рецепта")
        self.wait_non_empty_text_in_element(RecipeLocators.RECIPE_NAME)
        return self.find_element(RecipeLocators.RECIPE_NAME).text
