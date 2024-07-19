from conftest import driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import locators as loc
import helpers as helpers


class Registration:
    def __init__(self, driver):
        self.driver = driver

    def registration(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/register")

        # Ввод имени
        name_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc.name_input))
        name_input.send_keys(helpers.username)

        # Ввод email
        email_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc.reg_email_input))
        email_input.send_keys(helpers.registered_email)

        # Ввод пароля
        pwd_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(loc.auth_pwd_input))
        pwd_input.send_keys(helpers.user_password)

        # Нажатие на кнопку отправки формы
        submit_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc.auth_submit_btn))
        submit_btn.click()



def test_registration(driver):
    registration_page = Registration(driver)
    registration_page.registration()
