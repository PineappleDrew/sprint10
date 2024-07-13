import webbrowser
from conftest import driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from locators import Locators as loc


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
    def registration(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/register")

        username_input = self.driver.find_element(By.XPATH, loc.name_input)
        username_input.send_keys(loc.username)

        email_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, loc.email_input)))
        email_input.send_keys(loc.user_email)

        pwd_input = self.driver.find_element(By.XPATH, loc.password_input)
        pwd_input.send_keys(loc.user_password)

        submit_btn = self.driver.find_element(By.CSS_SELECTOR, loc.reg_btn )
        submit_btn.click()

        assert "Вход"

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login_account(self):
        login_btn = self.driver.find_element(By.XPATH, loc.loginAcc_btn)
        login_btn.click()
        assert "Вход"

    def login_persnl_acc(self):
        login_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, loc.loginPersAcc_btn))
        )
        login_btn.click()
        assert "Вход"

    def login_by_reg(self):
        login_btn = self.driver.find_element(By.CSS_SELECTOR, loc.entering_press)
        login_btn.click()
        assert "Вход"

    def login_by_res_pwd(self):
        res_pwd = self.driver.find_element(By.XPATH, loc.reset_password_button)
        res_pwd.click()
        assert "Вход"

class Authorization:
    def __init__(self, driver):
        self.driver = driver

    def authorization(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        LoginPage.login_account(self)

        # Ввод email
        email_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@type="text"]'))
        )
        email_input.send_keys(loc.registered_email)

        # Ввод пароля
        pwd_input = self.driver.find_element(By.XPATH, '//input[@type="password"]')
        pwd_input.send_keys(loc.user_password)

        # Нажатие на кнопку отправки формы
        submit_btn = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button')
        submit_btn.click()
class SwitchPage:
    def __init__(self, driver):
        self.driver = driver

    def switch_to_account(self):
        login_page = LoginPage(self.driver)
        login_page.login_account()

    def switch(self):
        # from time import sleep
        # Нажатие на кнопку аккаунта
        acc_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/header/nav/a'))
        )
        acc_btn.click()

        # Нажатие на кнопку конструктора
        kit_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a')))
        kit_btn.click()
        # sleep(10)

        # Проверка
        menu = self.driver.find_element(By.XPATH,
            '//div[@class="BurgerIngredients_ingredients__menuContainer__Xu3Mo"]')
        assert menu

        acc_btn.click()

        # Нажатие на кнопку бургеров
        burger_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]'))
        )
        burger_btn.click()
        assert menu


class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")  # Переход на страницу авторизации
        LoginPage.login_account(self)

        Authorization.authorization(self)

        # Нажатие на кнопку аккаунта
        acc_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/header/nav/a'))
        )
        acc_btn.click()

        # Ожидание появления и нажатие кнопки выхода из аккаунта
        logout_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, loc.logout_button))
        )
        logout_btn.click()

        # Проверка наличия формы авторизации после выхода из аккаунта
        assert "Вход"
class KitPage:
    def __init__(self, driver):
        self.driver = driver

    def switch_to_buns(self):
        buns_loc = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, loc.buns_loc))
        )
        self.driver.execute_script("arguments[0].click();", buns_loc)
        assert loc.buns

    def switch_to_sauces(self):
        sauces_loc = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, loc.sauces_loc))
        )
        self.driver.execute_script("arguments[0].click();", sauces_loc)
        assert loc.sauces

    def switch_to_fillings(self):
        fillings_loc = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, loc.fillings_loc))
        )
        self.driver.execute_script("arguments[0].click();", fillings_loc)
        assert loc.fillings





