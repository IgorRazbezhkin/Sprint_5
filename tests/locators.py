from selenium.webdriver.common.by import By


class Registration:
    personal_account_button = (By.XPATH, ".//*[@href='/account']")
    register_button = (By.XPATH, ".//*[@href='/register']")
    field_name = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")
    placeholder_name = (By.XPATH, ".//label[text()='Имя']")
    field_email = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    field_password = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
    button_to_complete_registration = (By.XPATH, ".//button[contains(text(), 'Зарегистрироваться')]")
    incorrect_password_error_message = (By.XPATH, ".//p[contains(text(), 'Некорректный пароль')]")

class Login:
    login_to_your_account_button = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    email_button_on_the_login_page = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    password_button_on_login_page = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
    login_button_on_login_page = (By.XPATH, ".//button[text()='Войти']")
    logout_button = (By.XPATH, ".//button[contains(text(), 'Выход')]")
    login_button_on_the_registration_and_password_recovery_page = (By.XPATH, ".//*[@href='/login']")
    recover_password_button = (By.XPATH, ".//*[@href='/forgot-password']")
    logo = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")

class ConstructorSection:
    button_constructor = (By.XPATH, ".//p[text()='Конструктор']")
    filling_section = (By.XPATH, ".//span[text()='Начинки']")
    sauces_section = (By.XPATH, ".//span[text()='Соусы']")
    bun_section = (By.XPATH, ".//span[text()='Булки']")
    filling_meat_of_the_immortal_mollusks_protostomia = (By.XPATH, ".//p[text()='Мясо бессмертных моллюсков Protostomia']")
    sauce_spicy_x = (By.XPATH, ".//p[text()='Соус Spicy-X']")
    bun_fluorescent_bun_r2_d3 = (By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3']")