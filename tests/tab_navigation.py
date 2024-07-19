from conftest import driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import locators as loc
import helpers as helpers

class Switch:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://stellarburgers.nomoreparties.site/")

    def authorization(self):

        # кнопка входа в аккаунт
        login_acc_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(loc.loginAcc_btn))
        login_acc_button.click()

        # Ввод email
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(loc.log_email_input))
        email_input.send_keys(helpers.registered_email)

        # Ввод пароля
        pwd_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(loc.auth_pwd_input))
        pwd_input.send_keys(helpers.user_password)

        # Нажатие на кнопку отправки формы
        log_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(loc.auth_submit_btn))
        log_btn.click()

    def switch_pers_acc(self):

        # аунтификация
        self.authorization()

        # вход в личный кабинет
        login_pers_acc_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(loc.loginPersAcc_btn))
        login_pers_acc_button.click()

    def switch_to_constructor(self):

        # вход в личный кабинет
        self.switch_pers_acc()

        # выход в конструктор
        constructor_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(loc.constructor_btn))
        constructor_button.click()




def test_switch_pers_acc(driver):
    switch_page = Switch(driver)
    switch_page.switch_pers_acc()

def test_switch_constructor(driver):
    switch_page = Switch(driver)
    switch_page.switch_to_constructor()

