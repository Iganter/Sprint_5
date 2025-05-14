from selenium.webdriver.support import expected_conditions as EC

from config import BASE_URL
from helpers.data_helpers import DataHelper


class TestRegistration:
    def test_register_new_user_success(
            self,
            create_driver,
            wait,
            home_locators,
            login_locators,
            registration_locators,
            account_locators
    ):
        create_driver.get(BASE_URL)

        # переходим по кнопке "Войти в аккаунт"
        wait.until(EC.element_to_be_clickable(home_locators.login_account_button)).click()

        # переходим по кнопке "Зарегистрироваться"
        wait.until(EC.element_to_be_clickable(login_locators.registration_link)).click()

        # вводим данные для регистрации
        name_data = DataHelper.generate_name()
        email_data = DataHelper.generate_login()
        password_data = DataHelper.generate_password()

        wait.until(EC.visibility_of_element_located(registration_locators.name_input)).send_keys(name_data)
        wait.until(EC.visibility_of_element_located(registration_locators.email_input)).send_keys(email_data)
        wait.until(EC.visibility_of_element_located(registration_locators.password_input)).send_keys(password_data)

        # нажимаем кнопку "Зарегистрироваться"
        wait.until(EC.element_to_be_clickable(registration_locators.register_button)).click()

        # проверяем, что страница авторизации загрузилась
        wait.until(EC.visibility_of_element_located(login_locators.login_label))

        # после регистрации авторизуемся с этими данными
        wait.until(EC.visibility_of_element_located(login_locators.login_input)).send_keys(email_data)
        wait.until(EC.visibility_of_element_located(login_locators.password_input)).send_keys(password_data)
        wait.until(EC.element_to_be_clickable(login_locators.login_button)).click()

        # переходим в личный кабинет
        wait.until(EC.element_to_be_clickable(home_locators.account_link)).click()

        # проверяем данные пользователя
        assert wait.until(
            EC.visibility_of_element_located(account_locators.name_input)
        ).get_attribute('value') == name_data
        assert wait.until(
            EC.visibility_of_element_located(account_locators.login_input)
        ).get_attribute('value') == email_data

    def test_registration_with_invalid_password_shows_error(
            self,
            create_driver,
            wait,
            home_locators,
            login_locators,
            registration_locators,
    ):
        create_driver.get(BASE_URL)

        # переходим по кнопке "Войти в аккаунт"
        wait.until(EC.element_to_be_clickable(home_locators.login_account_button)).click()

        # переходим по кнопке "Зарегистрироваться"
        wait.until(EC.element_to_be_clickable(login_locators.registration_link)).click()

        # вводим данные для регистрации, но короткий пароль
        name_data = DataHelper.generate_name()
        email_data = DataHelper.generate_login()
        password_data = '123'

        wait.until(EC.visibility_of_element_located(registration_locators.name_input)).send_keys(name_data)
        wait.until(EC.visibility_of_element_located(registration_locators.email_input)).send_keys(email_data)
        wait.until(EC.visibility_of_element_located(registration_locators.password_input)).send_keys(password_data)

        # пытаемся зарегистрироваться
        wait.until(EC.element_to_be_clickable(registration_locators.register_button)).click()

        # проверяем наличие ошибки
        assert wait.until(
            EC.visibility_of_element_located(registration_locators.password_error)
        ).text == 'Некорректный пароль'
