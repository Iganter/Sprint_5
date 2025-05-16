from selenium.webdriver.support import expected_conditions as EC

from config import BASE_URL

class TestLoginFlows:
    def test_login_from_main_page_via_button_success(
            self,
            create_driver,
            wait,
            home_locators,
            account_locators,
            login_locators,
            user_data
    ):
        create_driver.get(BASE_URL)

        # переходим по кнопке "Войти в аккаунт"
        wait.until(EC.element_to_be_clickable(home_locators.login_account_button)).click()

        # заполняем email и пароль
        wait.until(EC.visibility_of_element_located(login_locators.login_input)).send_keys(user_data.email)
        wait.until(EC.visibility_of_element_located(login_locators.password_input)).send_keys(user_data.password)

        # нажимаем "Войти"
        wait.until(EC.element_to_be_clickable(login_locators.login_button)).click()

        # переходим в "Личный кабинет"
        wait.until(EC.element_to_be_clickable(home_locators.account_link)).click()

        # проверяем данные пользователя
        assert wait.until(
            EC.visibility_of_element_located(account_locators.name_input)
        ).get_attribute('value') == user_data.name
        assert wait.until(
            EC.visibility_of_element_located(account_locators.login_input)
        ).get_attribute('value') == user_data.email

    def test_login_from_account_button_success(
            self,
            create_driver,
            wait,
            home_locators,
            account_locators,
            login_locators,
            user_data
    ):
        create_driver.get(BASE_URL)

        # переходим по кнопке "Личный кабинет"
        wait.until(EC.element_to_be_clickable(home_locators.account_link)).click()

        # заполняем email и пароль
        wait.until(EC.visibility_of_element_located(login_locators.login_input)).send_keys(user_data.email)
        wait.until(EC.visibility_of_element_located(login_locators.password_input)).send_keys(user_data.password)

        # нажимаем "Войти"
        wait.until(EC.element_to_be_clickable(login_locators.login_button)).click()

        # переходим в "Личный кабинет"
        wait.until(EC.element_to_be_clickable(home_locators.account_link)).click()

        # проверяем данные пользователя
        assert wait.until(
            EC.visibility_of_element_located(account_locators.name_input)
        ).get_attribute('value') == user_data.name
        assert wait.until(
            EC.visibility_of_element_located(account_locators.login_input)
        ).get_attribute('value') == user_data.email

    def test_login_from_registration_form_success(
            self,
            create_driver,
            wait,
            home_locators,
            account_locators,
            login_locators,
            registration_locators,
            user_data
    ):
        create_driver.get(BASE_URL)

        # переходим по кнопке "Войти в аккаунт"
        wait.until(EC.element_to_be_clickable(home_locators.login_account_button)).click()

        # переходим по кнопке "Зарегистрироваться"
        wait.until(EC.element_to_be_clickable(login_locators.registration_link)).click()

        # переходим по кнопке "Войти"
        wait.until(EC.element_to_be_clickable(registration_locators.login_button)).click()

        # заполняем email и пароль
        wait.until(EC.visibility_of_element_located(login_locators.login_input)).send_keys(user_data.email)
        wait.until(EC.visibility_of_element_located(login_locators.password_input)).send_keys(user_data.password)

        # нажимаем "Войти"
        wait.until(EC.element_to_be_clickable(login_locators.login_button)).click()

        # переходим в "Личный кабинет"
        wait.until(EC.element_to_be_clickable(home_locators.account_link)).click()

        # проверяем данные пользователя
        assert wait.until(
            EC.visibility_of_element_located(account_locators.name_input)
        ).get_attribute('value') == user_data.name
        assert wait.until(
            EC.visibility_of_element_located(account_locators.login_input)
        ).get_attribute('value') == user_data.email

    def test_login_from_restore_password_form_success(
            self,
            create_driver,
            wait,
            home_locators,
            account_locators,
            login_locators,
            restore_password_locators,
            user_data
    ):
        create_driver.get(BASE_URL)

        # переходим по кнопке "Войти в аккаунт"
        wait.until(EC.element_to_be_clickable(home_locators.login_account_button)).click()

        # переходим по кнопке "Восстановить пароль"
        wait.until(EC.element_to_be_clickable(login_locators.restore_password_link)).click()

        # переходим по кнопке "Войти"
        wait.until(EC.element_to_be_clickable(restore_password_locators.login_button)).click()

        # заполняем email и пароль
        wait.until(EC.visibility_of_element_located(login_locators.login_input)).send_keys(user_data.email)
        wait.until(EC.visibility_of_element_located(login_locators.password_input)).send_keys(user_data.password)

        # нажимаем "Войти"
        wait.until(EC.element_to_be_clickable(login_locators.login_button)).click()

        # переходим в "Личный кабинет"
        wait.until(EC.element_to_be_clickable(home_locators.account_link)).click()

        # проверяем данные пользователя
        assert wait.until(
            EC.visibility_of_element_located(account_locators.name_input)
        ).get_attribute('value') == user_data.name
        assert wait.until(
            EC.visibility_of_element_located(account_locators.login_input)
        ).get_attribute('value') == user_data.email
