from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from conftest import driver
from faker import Faker


class Locators:
    fake = Faker()

    name_input = '//input[@name="name"]'
    username = "Андрей"
    registered_email = "andreiprokurov7234@yandex.ru"

    email_input = '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input'
    user_email = fake.email() #Генерация случайного email с помощью faker

    password_input = '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input'
    user_password = "Razrazycheba123"

    submit_button = 'button'
    reg_btn = '.button_button__33qZ0 '

    loginAcc_btn = '//*/section[2]/div/button'
    loginPersAcc_btn = '//a[@href="/account"]'

     # Вход через кнопку в форме регистрации
    register_press = '//button[contains(text(), "Зарегистрироваться")]'

    entering_press = '.button_button__33qZ0 '

    # Вход через кнопку в форме восстановления пароля
    reset_password_button = '//a[@href="/forgot-password"]'

    # Проверка корректного перехода в личный кабинет
    account_btn = '//[href="/account"]'


    # Проверка перехода из ЛК при нажатии на Конструктор
    kit_loc = 'a.AppHeader_header__link__3D_hX'


    # Проверка перехода из ЛК при нажатии на Бургер
    burger_loc = '//div[@class="AppHeader_header__logo__2D0X2"]'

    # Проверка выхода из аккаунта
    logout_button = '.Account_button__14Yp3'

    #KIT locators
    buns_loc = '//*[@class="BurgerIngredients_ingredients__1N8v2"]/div/div[1]'
    buns = '//*[@class="BurgerIngredients_ingredients__menuContainer__Xu3Mo"]/h2[1]'

    sauces_loc = '//*[@class="BurgerIngredients_ingredients__1N8v2"]/div/div[2]'
    sauces = '//*[@class="BurgerIngredients_ingredients__menuContainer__Xu3Mo"]/h2[2]'

    fillings_loc = '//*[@class="BurgerIngredients_ingredients__1N8v2"]/div/div[3]'
    fillings = '//*[@class="BurgerIngredients_ingredients__menuContainer__Xu3Mo"]/h2[3]'