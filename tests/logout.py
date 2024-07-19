from conftest import driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import locators as loc
import helpers as helpers

class Logout:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://stellarburgers.nomoreparties.site/")

    def authorization(self):

        # кнопка входа в аккаунт
        login_acc_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(loc.loginAcc_btn))
        login_acc_button.click()

        # Ввод email
        email_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(loc.log_email_input))
        email_input.send_keys(helpers.registered_email)

        # Ввод пароля
        pwd_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(loc.auth_pwd_input))
        pwd_input.send_keys(helpers.user_password)

        # Нажатие на кнопку отправки формы
        log_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(loc.auth_submit_btn))
        log_btn.click()

    def logout_acc(self):

        # аунтификация
        self.authorization()

        #вход в личный кабинет
        login_pers_acc_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(loc.loginPersAcc_btn))
        login_pers_acc_button.click()

        #выход с аккаунта
        logout_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(loc.logout_btn))
        logout_button.click()

def test_logout_account(driver):
    logout = Logout(driver)
    logout.logout_acc()

