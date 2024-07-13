import time
from selenium import webdriver
import webbrowser
from conftest import driver
import pytest
from pages import RegistrationPage, LoginPage, SwitchPage, LogoutPage, KitPage, Authorization

# Проверка успешной регистрации
def test_successful_registration(driver):
    reg_page = RegistrationPage(driver)
    driver.get("https://stellarburgers.nomoreparties.site")
    reg_page.registration()


def test_login_main(driver):
    log_page = LoginPage(driver)
    driver.get("https://stellarburgers.nomoreparties.site")
    log_page.login_account()

def test_login_account(driver):
    log_page = LoginPage(driver)
    driver.get("https://stellarburgers.nomoreparties.site")
    log_page.login_persnl_acc()

def test_login_reg(driver):
    log_page = LoginPage(driver)
    driver.get("https://stellarburgers.nomoreparties.site/register")
    log_page.login_by_reg()

def test_login_resPwd(driver):
    log_page = LoginPage(driver)
    driver.get("https://stellarburgers.nomoreparties.site/login")
    log_page.login_by_res_pwd()

def test_switch_to_acc(driver):
    switch_page = SwitchPage(driver)
    driver.get("https://stellarburgers.nomoreparties.site")
    switch_page.switch_to_account()

def test_switch(driver):
    switch_page = SwitchPage(driver)
    auth = Authorization(driver)

    auth.authorization()
    switch_page.switch()


def test_logout(driver):
    logout_page = LogoutPage(driver)

    logout_page.logout()

def test_burger_constructor(driver):
    kit_page = KitPage(driver)
    driver.get("https://stellarburgers.nomoreparties.site")
    kit_page.switch_to_buns()
    kit_page.switch_to_sauces()
    kit_page.switch_to_fillings()
