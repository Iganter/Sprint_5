from selenium.webdriver.common.by import By


class HomePageLocators:
    login_account_button = (By.XPATH, '//button[text() = "Войти в аккаунт"]')
    account_link = (By.XPATH, '//a[@href = "/account"]')

    buns_tab = (By.XPATH, '//span[text() = "Булки"]')
    sauces_tab = (By.XPATH, '//span[text() = "Соусы"]')
    fillings_tab = (By.XPATH, '//span[text() = "Начинки"]')

    buns_section = (By.XPATH, '//h2[text() = "Булки"]')
    sauces_section = (By.XPATH, '//h2[text()= "Соусы"]')
    fillings_section = (By.XPATH, '//h2[text() = "Начинки"]')

class RegistrationPageLocators:
    name_input = (By.XPATH, '//label[text() = "Имя"]/following-sibling::input')
    email_input = (By.XPATH, '//label[text() = "Email"]/following-sibling::input')
    password_input = (By.XPATH, '//label[text() = "Пароль"]/following-sibling::input')
    register_button = (By.XPATH, '//button[text() = "Зарегистрироваться"]')
    login_button = (By.XPATH, '//a[@href = "/login"]')
    password_error = (By.XPATH, '//p[text() = "Некорректный пароль"]')

class LoginPageLocators:
    login_label = (By.XPATH, '//h2[text() = "Вход"]')
    login_input = (By.XPATH, '//label[text() = "Email"]/following-sibling::input')
    password_input = (By.XPATH, '//label[text() = "Пароль"]/following-sibling::input')
    login_button = (By.XPATH, '//button[text() = "Войти"]')
    registration_link = (By.XPATH, '//a[@href="/register"]')
    restore_password_link = (By.XPATH, '//a[@href="/forgot-password"]')

class AccountPageLocators:
    name_input = (By.XPATH, '//label[text() = "Имя"]/following-sibling::input')
    login_input = (By.XPATH, '//label[text() = "Логин"]/following-sibling::input')
    password_input = (By.XPATH, '//label[text() = "Пароль"]/following-sibling::input')
    logout_button = (By.XPATH, '//button[text() = "Выход"]')
    logo_button = (By.XPATH, '(//a[@href="/"])[1]')
    constructor_button = (By.XPATH, '(//a[@href="/"])[2]')

class RestorePasswordPageLocators:
    login_button = (By.XPATH, '//a[@href = "/login"]')
