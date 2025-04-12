from pathlib import Path


class TestData:
    # Папка корня проекта
    BASE_DIR = Path(__file__).resolve().parent.parent.parent

    PHOTO = BASE_DIR / "src" / "data" / "namo-food.png"

    USER_NAME = 'Иван'
    USER_SURNAME = 'Иванов'

    INGREDIENT = 'молоко'
    WEIGHT = 100
    COOKING_TIME = 45
    RECIPE_DESCRIPTION = 'Очень увлекательное описание рецепта'

    USER_EMAIL = 'namo-yandex@test.test'
    USER_PASSWORD = 'namonamo_12345'
