from conftest import driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import locators as loc
import helpers as helpers


class Authorization:
    def __init__(self, driver):
        self.driver = driver

    def filling_form(self):

        # Ввод email
        email_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(loc.log_email_input))
        email_input.send_keys(helpers.registered_email)

        # Ввод пароля
        pwd_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(loc.auth_pwd_input))
        pwd_input.send_keys(helpers.user_password)

        # Нажатие на кнопку отправки формы
        log_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(loc.auth_submit_btn))
        log_btn.click()
    def authorization_main(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")

        # основная кнопка входа
        login_acc_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc.loginAcc_btn))
        login_acc_button.click()

        # заполнение формы
        self.filling_form()

    def authorization_acc(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")

        # вход через личный аккаунт
        login_pers_acc_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc.loginPersAcc_btn))
        login_pers_acc_button.click()

        # заполнение формы
        self.filling_form()

    def authorization_reg(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/register")

        # вход через страницу регистрации
        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc.login_btn))
        login_button.click()

        # заполнение формы
        self.filling_form()

    def authorization_forgot_pwd(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

        # вход через страницу смены пароля
        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc.login_btn))
        login_button.click()


def test_authorization(driver):
    authorization_page = Authorization(driver)
    authorization_page.authorization_main()

def test_authorization_acc(driver):
    authorization_page = Authorization(driver)
    authorization_page.authorization_acc()

def test_authorization_reg(driver):
    authorization_page = Authorization(driver)
    authorization_page.authorization_reg()

def test_authorization_forgot_pwd(driver):
    authorization_page = Authorization(driver)
    authorization_page.authorization_forgot_pwd()