import webbrowser
from conftest import driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from locators import Locators as loc
from locators import Helpers as helpers

class Checks:
    def __init__(self, driver):
        self.driver = driver
    def main_is_visible(self):
        menu_main_visible = EC.visibility_of_element_located(loc.menu_loc)
        menu_main = WebDriverWait(self.driver, 10).until(menu_main_visible)

        assert menu_main



    def login_form_is_exsits(self):
        login_form_locator = (By.XPATH, '//form[@class="Auth_form__3qKeq mb-20"]')
        login_form = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(login_form_locator))
        assert login_form

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
    def registration(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/register")

        email_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc.email_input))
        email_input.send_keys(helpers.user_email)

        username_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc.name_input))
        username_input.send_keys(helpers.username)


        pwd_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc.password_input))
        pwd_input.send_keys(helpers.user_password)

        reg_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc.reg_btn))
        reg_btn.click()

        Checks.login_form_is_exsits(self)


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login_account(self):
        login_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc.loginAcc_btn))
        login_btn.click()

        Checks.login_form_is_exsits(self)



    def login_persnl_acc(self):
        login_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(loc.loginPersAcc_btn))
        login_btn.click()

        Checks.login_form_is_exsits(self)

    def login_by_reg(self):
        login_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(loc.entering_press))
        login_btn.click()

        Checks.login_form_is_exsits(self)

    def login_by_res_pwd(self):
        res_pwd = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(loc.reset_password_button))
        res_pwd.click()
        Checks.login_form_is_exsits(self)

class Authorization:
    def __init__(self, driver):
        self.driver = driver

    def authorization(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        LoginPage.login_account(self)

        # Ввод email
        email_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc.auth_email_input))
        email_input.send_keys(helpers.registered_email)

        # Ввод пароля
        pwd_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc.auth_pwd_input))
        pwd_input.send_keys(helpers.user_password)

        # Нажатие на кнопку отправки формы
        submit_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc.auth_submit_btn))
        submit_btn.click()
class SwitchPage:
    def __init__(self, driver):
        self.driver = driver

    def switch_to_account(self):
        login_page = LoginPage(self.driver)
        login_page.login_account()

    def switch(self):
        # Нажатие на кнопку аккаунта
        acc_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(loc.account_btn))
        acc_btn.click()

        # Нажатие на кнопку конструктора
        kit_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(loc.kit_loc))
        kit_btn.click()


        # Проверка
        Checks.main_is_visible(self)

        acc_btn.click()

        # Нажатие на кнопку бургеров
        burger_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(loc.burger_loc))
        burger_btn.click()

        Checks.main_is_visible(self)


class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")  # Переход на страницу авторизации
        LoginPage.login_account(self)

        Authorization.authorization(self)

        # Нажатие на кнопку аккаунта
        acc_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(loc.account_btn)
        )
        acc_btn.click()

        # Ожидание появления и нажатие кнопки выхода из аккаунта
        logout_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(loc.logout_button))

        logout_btn.click()

        # Проверка наличия формы авторизации после выхода из аккаунта
        Checks.login_form_is_exsits(self)
class KitPage:
    def __init__(self, driver):
        self.driver = driver

    def switch_to_buns(self):
        buns_loc = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(loc.buns_loc))

        self.driver.execute_script("arguments[0].click();", buns_loc)
        assert loc.buns

    def switch_to_sauces(self):
        sauces_loc = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(loc.sauces_loc))

        self.driver.execute_script("arguments[0].click();", sauces_loc)
        assert loc.sauces

    def switch_to_fillings(self):
        fillings_loc = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(loc.fillings_loc))

        self.driver.execute_script("arguments[0].click();", fillings_loc)
        assert loc.fillings
