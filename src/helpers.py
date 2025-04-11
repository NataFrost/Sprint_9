import random
import string
import allure


# функция для генерации случайного адреса электронной почты
def random_email():
    domains = ["gmail.com", "yandex.ru", "mail.ru", "telekom.ru", "rambler.ru"]
    name_length = random.randint(5, 10)  # длина имени от 5 до 12 символов
    domain = random.choice(domains)
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=name_length))
    return f"namo-{name}@{domain}"


# функция для генерации случайного пароля
def random_password():
    password_length = random.randint(8, 12)  # длина пароля от 8 до 12 символов
    return ''.join(random.choices(string.ascii_letters + string.digits, k=password_length))


# функция для генерации случайного имени
def random_username():
    return 'namo-' + str(random.randint(10, 1000))


def get_sign_up_data():
    username = random_username()
    email = random_email()
    password = random_password()
    return username, email, password


def generate_recipe_name():
    # Базы данных для генерации
    adjectives = [
        "Аппетитный", "Ароматный", "Нежный", "Хрустящий", "Пикантный",
        "Итальянский", "Домашний", "Фирменный", "Праздничный", "Диетический"
    ]

    ingredients = [
        "куриный", "говяжий", "овощной", "сырный", "грибной",
        "картофельный", "морковный", "лососевый", "яблочный", "шоколадный"
    ]

    dish_types = [
        "суп", "салат", "пирог", "стейк", "десерт",
        "соус", "жульен", "крем", "мусс", "компот"
    ]

    # Дополнительные варианты
    cooking_styles = [
        "по-деревенски", "по-итальянски", "а-ля прованс", "от шеф-повара",
        "с хрустящей корочкой", "в сливочном соусе", "с пряными травами"
    ]

    # Генерация вариантов
    pattern = random.choice([
        f"{random.choice(adjectives)} {random.choice(ingredients)} {random.choice(dish_types)}",
        f"{random.choice(adjectives)} {random.choice(dish_types)} {random.choice(cooking_styles)}",
        f"{random.choice(ingredients)} {random.choice(dish_types)} {random.choice(cooking_styles)}",
        f"{random.choice(adjectives)} {random.choice(dish_types)} с {random.choice(ingredients).replace('ный', 'ом')}",
        f"{random.choice(['Тайский', 'Мексиканский', 'Французский', 'Японский'])} {random.choice(dish_types)}"
    ])

    return pattern.capitalize()


def allure_attach(actual_result, expected_result, field='Placeholder'):
    allure.attach(f'Field: {field},\nActual result: {actual_result},\nExpected result: {expected_result} ',
                    name="Детали проверки",
                    attachment_type=allure.attachment_type.TEXT
                    )
