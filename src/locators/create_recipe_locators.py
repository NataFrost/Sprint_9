from selenium.webdriver.common.by import By


class CreateRecipeLocators:

    CREATE_RECIPE_HEADER = (By.XPATH, ".//a[@href='/recipes/create']")
    BUTTON_CREATE_RECIPE = (By.XPATH, ".//form/button")
    INGREDIENT_INPUT = (By.XPATH, ".//input[contains(@class, 'ingredientsInput')]")
    AMOUNT_INPUT = (By.XPATH, ".//input[contains(@class, 'ingredientsAmountValue')]")
    TIME_INPUT = (By.XPATH, ".// div[contains(@class, 'ingredientsTimeInput')]//input")
    INGREDIENT_ADD_LINK = (By.XPATH, ".//div[contains(@class , 'ingredientAdd')]")
    SELECT_FILE = (By.XPATH, ".//div[@type='button']")
    INPUT_FILE = (By.XPATH, ".//input[@type='file']")
    RECIPE_NAME_INPUT = (By.XPATH, ".//div[text()='Название рецепта']/following-sibling::input")
    RECIPE_DESCRIPTION_INPUT = (By.XPATH, ".//textarea[contains(@class, 'textareaField')]")
    INGREDIENTS_DROPDOWN = (By.XPATH, ".//div[contains(@class, 'styles_container') and not (contains(@class, 'styles_fileInput'))]")
    INGREDIENTS_DROPDOWN_LIST = (
    By.XPATH, ".//div[contains(@class, 'styles_container') and not (contains(@class, 'styles_fileInput'))]/div")
