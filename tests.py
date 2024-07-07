from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Locators:
    NAME_INPUT = (By.XPATH, "//input[@name='name']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    REGISTRATION_SUCCESS_MESSAGE = (By.XPATH, "//div[@class='success-message']")
    LOGIN_SUCCESS_MESSAGE = (By.XPATH, "//div[@class='welcome-message']")
    USER_PROFILE_LINK = (By.XPATH, "//a[contains(@href,'/profile')]")
    FILLINGS_LINK = (By.XPATH, "//a[@href='/fillings']")
    FILLINGS_PAGE_TITLE = (By.XPATH, "//h1[contains(text(), 'Начинки')]")

def test_successful_registration():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")

    email_input = driver.find_element(*Locators.NAME_INPUT)
    email_input.send_keys("andrew")

    email_input = driver.find_element(*Locators.EMAIL_INPUT)
    email_input.send_keys("andreiprokurov7234@yandex.ru")

    password_input = driver.find_element(*Locators.PASSWORD_INPUT)
    password_input.send_keys("razrazycheba123")

    submit_button = driver.find_element(*Locators.SUBMIT_BUTTON)
    submit_button.click()

    wait = WebDriverWait(driver, 10)
    success_message = wait.until(EC.url_contains("https://stellarburgers.nomoreparties.site/login"))
    assert success_message

    driver.quit()

def test_login():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")

    email_input = driver.find_element(*Locators.EMAIL_INPUT)
    email_input.send_keys("test@example.com")

    password_input = driver.find_element(*Locators.PASSWORD_INPUT)
    password_input.send_keys("password123")

    submit_button = driver.find_element(*Locators.SUBMIT_BUTTON)
    submit_button.click()

    wait = WebDriverWait(driver, 10)
    success_message = wait.until(EC.visibility_of_element_located(Locators.LOGIN_SUCCESS_MESSAGE))
    assert success_message.text == "Добро пожаловать, test@example.com!"

    driver.implicitly_wait(2)

    user_profile_link = driver.find_element(*Locators.USER_PROFILE_LINK)
    assert user_profile_link.text == "Профиль пользователя"

    driver.quit()

def test_burger_constructor():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")

    fillings_link = driver.find_element(*Locators.FILLINGS_LINK)
    fillings_link.click()

    wait = WebDriverWait(driver, 10)
    fillings_page_title = wait.until(EC.visibility_of_element_located(Locators.FILLINGS_PAGE_TITLE))
    assert fillings_page_title.text == "Начинки для бургеров"

    driver.quit()


