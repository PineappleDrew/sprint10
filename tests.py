import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome()



driver.get("https://stellarburgers.nomoreparties.site")


# Проверка успешной регистрации

def test_successful_registration():
    name_input = driver.find_element(By.XPATH, '//input[@name="name"]')

    name_input.send_keys("Андрей")

    email_input = driver.find_element(By.XPATH, '//input[@name="email"]')

    email_input.send_keys("andreiprokurov7234@yandex.ru")

    password_input = driver.find_element(By.XPATH, '//input[@name="password"]')

    password_input.send_keys("Razrazycheba123")

    submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')

    submit_button.click()

    time.sleep(2)  # Пауза для проверки результата



# Тестирование функциональности "Вход"

def test_login():
    # Вход по кнопке «Войти в аккаунт» на главной

    login_button = driver.find_element(By.XPATH, '//button[contains(text(), "Войти в аккаунт")]')

    login_button.click()

    # Вход через кнопку «Личный кабинет»

    login_button = driver.find_element(By.XPATH, '//button[contains(text(), "Личный кабинет")]')

    login_button.click()

    # Вход через кнопку в форме регистрации

    register_button = driver.find_element(By.XPATH, '//button[contains(text(), "Личный Кабинет")]')

    register_button.click()

    register_press = driver.find_element(By.XPATH, '//button[contains(text(), "Зарегестрироваться")]')

    register_press.click()

    enterning_press = driver.find_element(By.XPATH, '//button[contains(text(), "Войти")]')

    enterning_press.click()

    email_input = driver.find_element(By.XPATH, '//input[@name="email"]')

    email_input.send_keys("andreiprokurov7234@yandex.ru")

    password_input = driver.find_element(By.XPATH, '//input[@name="password"]')

    password_input.send_keys("Razrazycheba123")

    submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')

    submit_button.click()

    # Вход через кнопку в форме восстановления пароля

    reset_password_button = driver.find_element(By.XPATH, '//button[contains(text(), "Восстановить пароль")]')

    reset_password_button.click()

    email_input = driver.find_element(By.XPATH, '//input[@name="email"]')

    email_input.send_keys("andreiprokurov7234@yandex.ru")

    submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')

    submit_button.click()

    time.sleep(2)

    # Проверка перехода в личный кабинет

    personal_account_link = driver.find_element(By.XPATH, '//a[@href="/profile"]')

    personal_account_link.click()

    time.sleep(2)

    # Проверка перехода из личного кабинета в конструктор

    constructor_link = driver.find_element(By.XPATH, '//a[@href="/burger-constructor"]')

    constructor_link.click()

    time.sleep(2)

    # Проверка выхода из аккаунта

    logout_button = driver.find_element(By.XPATH, '//button[contains(text(), "Выйти")]')

    logout_button.click()


# Тестирование раздела "Конструктор"

def test_burger_constructor():
    # Проверка перехода к разделу "Булки"

    buns_link = driver.find_element(By.XPATH, '//a[@href="/burger-constructor/buns"]')

    buns_link.click()

    time.sleep(2)

    # Проверка перехода к разделу "Соусы"

    sauces_link = driver.find_element(By.XPATH, '//a[@href="/burger-constructor/sauces"]')

    sauces_link.click()

    time.sleep(2)

    # Проверка перехода к разделу "Начинки"

    fillings_link = driver.find_element(By.XPATH, '//a[@href="/burger-constructor/fillings"]')

    fillings_link.click()

    time.sleep(2)



test_successful_registration()

test_login()

test_burger_constructor()

driver.quit()