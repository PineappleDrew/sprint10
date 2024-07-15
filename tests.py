from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from conftest import driver
from faker import Faker

class Helpers:
    fake = Faker()
    username = "Андрей"
    registered_email = "andreiprokurov7234@yandex.ru"
    user_email = fake.email()  # Генерация случайного email с помощью faker
    user_password = "Razrazycheba123"

class Locators:
    name_input = (By.XPATH, '//input[@name="name"]')
    email_input = (By.XPATH, "//form[contains(@class, 'Auth_form__3qKeq')]//fieldset[contains(@class, 'Auth_fieldset__1QzWN')][2]"
                             "//input[@type='text' and @name='name']")
    auth_email_input = (By.XPATH, '//input[@type="text"]')
    auth_pwd_input = (By.XPATH, '//input[@name="Пароль"]')
    password_input = (By.XPATH, '//input[@type="password"]')

    submit_button = (By.CSS_SELECTOR, '.button_button_size_medium__3zxIa')
    auth_submit_btn = (By.XPATH, '//button[contains(@class, "button_button_type_primary__1O7Bx") and contains(@class, "button_button_size_medium__3zxIa")]')
    reg_btn = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')

    loginAcc_btn = (By.XPATH, '//*/section[2]/div/button')
    loginPersAcc_btn = (By.XPATH, '//a[@href="/account"]')

    # Вход через кнопку в форме регистрации
    register_press = (By.XPATH, '//button[contains(text(), "Зарегистрироваться")]')

    entering_press = (By.CSS_SELECTOR, '.button_button__33qZ0')

    # Вход через кнопку в форме восстановления пароля
    reset_password_button = (By.XPATH, '//a[@href="/forgot-password"]')

    menu_loc = (By.XPATH, '//div[@class="BurgerIngredients_ingredients__menuContainer__Xu3Mo"]')

    # Проверка корректного перехода в личный кабинет
    account_btn = (By.XPATH, '//*[@href="/account"]')

    # Проверка перехода из ЛК при нажатии на Конструктор
    kit_loc = (By.XPATH, '//p[text()="Конструктор"]')

    # Проверка перехода из ЛК при нажатии на Бургер
    burger_loc = (By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]')

    # Проверка выхода из аккаунта
    logout_button = (By.CSS_SELECTOR, '.Account_button__14Yp3')

    # KIT locators
    buns_loc = (By.XPATH, '//span[text()="Булки"]')
    buns = (By.XPATH, '//ul[contains(@class, "BurgerIngredients_ingredients__list__2A-mT")]//a[contains(., "булка")]')

    sauces_loc = (By.XPATH, '//span[text()="Соусы"]')
    sauces = (By.XPATH, '//ul[contains(@class, "BurgerIngredients_ingredients__list__2A-mT")]//a[contains(., "Соус")]')

    fillings_loc = (By.XPATH, '//span[text()="Начинки"]')
    fillings = (By.XPATH, '//h2[@class="text text_type_main-medium mb-6 mt-10" and text()="Начинки"]')
