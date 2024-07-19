from selenium.webdriver.common.by import By

# поле ввода имени
name_input = (By.XPATH, '//input[@name="name"]')

# поле ввода почты при регистрации
email_input = (By.XPATH, "//form[contains(@class, 'Auth_form__3qKeq')]//fieldset[contains(@class, 'Auth_fieldset__1QzWN')][2]" "//input[@type='text' and @name='name']")

# поле ввода регистрации
reg_email_input = (By.XPATH, '(//input[contains(@name, "name")])[2]')

# поле ввода пароля
auth_pwd_input = (By.XPATH, '//input[@name="Пароль"]')

# кнопка отправки формы
auth_submit_btn = (By.XPATH, '//button[contains(@class, "button_button__33qZ0") and contains(@class, "button_button_type_primary__1O7Bx") and contains(@class, "button_button_size_medium__3zxIa")]')

# кнопка входа на главной странице
loginAcc_btn = (By.XPATH, '//button[contains(@class, "button_button__33qZ0") and contains(@class, "button_button_type_primary__1O7Bx") and contains(@class, "button_button_size_large__G21Vg")]')

# поле ввода почты при входе в аккаунт
log_email_input = (By.XPATH, '//input[@name="name"]')

# кнопка входа в личный кабинет
loginPersAcc_btn = (By.XPATH, '//a[@href="/account"]')

# кнопка входа на странице регистрации
login_btn = (By.XPATH, '//a[@href="/login"]')

# кнопка перехода в конструктор
constructor_btn = (By.XPATH, '//a[@href="/"]')

# кнопка выхода из аккаунта
logout_btn = (By.XPATH, '//button[contains(text(), "Выход")]')

# кнопка 'Булки' в конструкторе
buns_loc = (By.XPATH, '//span[text()="Булки"]')

# кнопка 'Соусы' в конструкторе
sauces_loc = (By.XPATH, '//span[text()="Соусы"]')

# кнопка 'Начинка' в конструкторе
fillings_loc = (By.XPATH, '//span[text()="Начинки"]')
