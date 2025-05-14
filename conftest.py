import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test_data.test_data import UserData
from locators.all_locators import (
    HomePageLocators,
    LoginPageLocators,
    RegistrationPageLocators,
    RestorePasswordPageLocators,
    AccountPageLocators
)
from config import BASE_URL


@pytest.fixture(scope='function')
def create_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()

@pytest.fixture
def home_locators():
    return HomePageLocators()

@pytest.fixture
def login_locators():
    return LoginPageLocators()

@pytest.fixture
def registration_locators():
    return RegistrationPageLocators()

@pytest.fixture
def restore_password_locators():
    return RestorePasswordPageLocators()

@pytest.fixture
def account_locators():
    return AccountPageLocators()

@pytest.fixture
def user_data():
    return UserData()

@pytest.fixture(scope='function')
def wait(create_driver):
    return WebDriverWait(create_driver, 10)

@pytest.fixture
def login(create_driver, wait, user_data, home_locators, login_locators):
    # переходим на главную
    create_driver.get(BASE_URL)

    # нажимаем "Войти в аккаунт"
    wait.until(EC.element_to_be_clickable(home_locators.login_account_button)).click()

    # заполняем email и пароль
    wait.until(EC.visibility_of_element_located(login_locators.login_input)).send_keys(user_data.email)
    wait.until(EC.visibility_of_element_located(login_locators.password_input)).send_keys(user_data.password)

    # нажимаем "Войти"
    wait.until(EC.element_to_be_clickable(login_locators.login_button)).click()
