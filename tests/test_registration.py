from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers.data_helpers import DataHelper
from locators.all_locators import (
    HomePageLocators,
    RegistrationPageLocators,
    LoginPageLocators,
    AccountPageLocators
)


home_locators = HomePageLocators()
login_locators = LoginPageLocators()
registration_locators = RegistrationPageLocators()
account_locators = AccountPageLocators()


class TestRegistration:
    def test_register_new_user(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        # переходим на главную страницу
        driver.get('https://stellarburgers.nomoreparties.site/')
        sleep(3)

        # переходим по кнопке "Войти в аккаунт"
        login_account_button = wait.until(EC.element_to_be_clickable(home_locators.login_account_button))
        login_account_button.click()
        sleep(3)

        # переходим по кнопке "Зарегистрироваться"
        registration_link = wait.until(EC.element_to_be_clickable(login_locators.registration_link))
        registration_link.click()
        sleep(3)

        # вводим данные для регистрации
        name_data = DataHelper.generate_name()
        email_data = DataHelper.generate_login()
        password_data = DataHelper.generate_password()

        register_name_input = wait.until(EC.visibility_of_element_located(registration_locators.name_input))
        register_email_input = wait.until(EC.visibility_of_element_located(registration_locators.email_input))
        register_password_input = wait.until(EC.visibility_of_element_located(registration_locators.password_input))

        register_name_input.send_keys(name_data)
        register_email_input.send_keys(email_data)
        register_password_input.send_keys(password_data)

        register_button = wait.until(EC.element_to_be_clickable(registration_locators.register_button))
        register_button.click()
        sleep(3)

        # после регистрации попадаем на вход и проверяем введенные данные
        login_input = wait.until(EC.visibility_of_element_located(login_locators.login_input))
        password_input = wait.until(EC.visibility_of_element_located(login_locators.password_input))

        login_input.send_keys(email_data)
        password_input.send_keys(password_data)

        login_button = wait.until(EC.element_to_be_clickable(login_locators.login_button))
        login_button.click()
        sleep(3)

        # переходим в личный кабинет
        account_link = wait.until(EC.element_to_be_clickable(home_locators.account_link))
        account_link.click()
        sleep(3)

        # проверяем данные пользователя
        account_name_input = wait.until(EC.visibility_of_element_located(account_locators.name_input))
        account_login_input = wait.until(EC.visibility_of_element_located(account_locators.login_input))

        assert account_name_input.get_attribute('value') == name_data
        assert account_login_input.get_attribute('value') == email_data
