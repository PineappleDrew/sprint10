from conftest import driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import locators as loc

class Navigation_constructor:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://stellarburgers.nomoreparties.site/")

    def buns(self):

        # показать соусы
        sauces_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(loc.sauces_loc))
        sauces_btn.click()

        # показать булки
        buns_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(loc.buns_loc))
        buns_btn.click()

    def sauces(self):

        # показать соусы
        sauces_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(loc.sauces_loc))
        sauces_btn.click()

    def filling(self):

        # показать начинку
        filling_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(loc.fillings_loc))
        filling_btn.click()




def test_navigation_buns(driver):
    navigation_buns = Navigation_constructor(driver)
    navigation_buns.buns()

def test_navigation_sauces(driver):
    navigation_sauces = Navigation_constructor(driver)
    navigation_sauces.sauces()

def test_navigation_filling(driver):
    navigation_filling = Navigation_constructor(driver)
    navigation_filling.filling()
