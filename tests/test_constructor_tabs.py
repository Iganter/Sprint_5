from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test_data.test_data import UserData
from locators.all_locators import (
    HomePageLocators,
    LoginPageLocators,
    AccountPageLocators
)

home_locators = HomePageLocators()
login_locators = LoginPageLocators()
account_locators = AccountPageLocators()
user_data = UserData()

def test_constructor_tabs(create_driver):
    driver = create_driver
    wait = WebDriverWait(driver, timeout=10)

    # переходим на главную страницу
    driver.get('https://stellarburgers.nomoreparties.site/')
    sleep(3)

    # переходим по кнопке "Войти в аккаунт"
    login_account_button = wait.until(EC.element_to_be_clickable(home_locators.login_account_button))
    login_account_button.click()
    sleep(3)

    login_input = wait.until(EC.visibility_of_element_located(login_locators.login_input))
    password_input = wait.until(EC.visibility_of_element_located(login_locators.password_input))

    login_input.send_keys(user_data.email)
    password_input.send_keys(user_data.password)
    sleep(3)

    login_button = wait.until(EC.element_to_be_clickable(login_locators.login_button))
    login_button.click()
    sleep(3)

    # кликаем по разделу "Соусы"
    sauces_tab = wait.until(EC.element_to_be_clickable(home_locators.sauces_tab))
    sauces_tab.click()
    assert wait.until(EC.visibility_of_element_located(home_locators.sauces_section))
    sleep(3)

    # Клик по разделу "Начинки"
    fillings_tab = wait.until(EC.element_to_be_clickable(home_locators.fillings_tab))
    fillings_tab.click()
    assert wait.until(EC.visibility_of_element_located(home_locators.fillings_section))
    sleep(3)

    # Клик по разделу "Булки"
    buns_tab = wait.until(EC.element_to_be_clickable(home_locators.buns_tab))
    buns_tab.click()
    assert wait.until(EC.visibility_of_element_located(home_locators.buns_section))
    sleep(3)
