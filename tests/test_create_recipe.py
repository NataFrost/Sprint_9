import allure

from src.pages.page_create_recipe import PageCreateRecipe
from src.pages.page_recipe import RecipePage

from src.data.data import TestData
from src.helpers import generate_recipe_name, allure_attach


class TestCreateRecipe:

    def test_create_recipe(self, driver, login_new_user):
        recipe_name = generate_recipe_name()
        page = PageCreateRecipe(driver)
        page.open_create_recipe_page()
        page.enter_receipt_name(recipe_name)
        page.select_ingredient(TestData.INGREDIENT)
        page.enter_weight(TestData.WEIGHT)
        page.add_ingredient()
        page.enter_cooking_time(TestData.COOKING_TIME)
        page.enter_recipe_description(TestData.RECIPE_DESCRIPTION)
        page.upload_photo(TestData.PHOTO)
        page.create_recipe()

        recipe_page = RecipePage(driver)

        with allure.step("Проверка, что имя рецепта правильное"):
            assert recipe_name == recipe_page.get_recipe_name()
            allure_attach(recipe_page.get_recipe_name(), recipe_name, "Название рецепта")
