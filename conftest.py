import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    # Инициализация веб-драйвера
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver  # Этот блок выполнится после завершения тестов
