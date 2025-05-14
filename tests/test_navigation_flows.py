import pytest
from selenium.webdriver.support import expected_conditions as EC


class TestNavigationFlows:
    @pytest.mark.usefixtures('login')
    def test_sauces_tab_opens_section(self, create_driver, wait, home_locators):

        # кликаем по разделу "Соусы"
        wait.until(EC.element_to_be_clickable(home_locators.sauces_tab)).click()
        assert wait.until(EC.visibility_of_element_located(home_locators.sauces_section))

    @pytest.mark.usefixtures('login')
    def test_fillings_tab_opens_section(self, create_driver, wait, home_locators):

        # кликаем по разделу "Начинки"
        wait.until(EC.element_to_be_clickable(home_locators.fillings_tab)).click()
        assert wait.until(EC.visibility_of_element_located(home_locators.fillings_section))

    @pytest.mark.usefixtures('login')
    def test_buns_tab_opens_section(self, create_driver, wait, home_locators):

        # сперва переключаемся на вкладку "Соусы", чтобы увести фокус
        wait.until(EC.element_to_be_clickable(home_locators.sauces_tab)).click()
        wait.until(EC.visibility_of_element_located(home_locators.sauces_section))

        # теперь возвращаемся и кликаем по разделу "Булки"
        wait.until(EC.element_to_be_clickable(home_locators.buns_tab)).click()
        assert wait.until(EC.visibility_of_element_located(home_locators.buns_section))

    @pytest.mark.usefixtures('login')
    def test_go_to_profile_from_main_page(self, create_driver, wait, home_locators, account_locators, user_data):

        # переходим в профиль по клику на "Личный кабинет"
        wait.until(EC.element_to_be_clickable(home_locators.account_link)).click()
        assert wait.until(
            EC.visibility_of_element_located(account_locators.name_input)
        ).get_attribute('value') == user_data.name
        assert wait.until(
            EC.visibility_of_element_located(account_locators.login_input)
        ).get_attribute('value') == user_data.email

    @pytest.mark.usefixtures('login')
    def test_go_to_constructor_from_profile_via_button(self, create_driver, wait, home_locators, account_locators):

        # переходим в профиль по клику на "Личный кабинет"
        wait.until(EC.element_to_be_clickable(home_locators.account_link)).click()

        # переходим из личного кабинета в "Конструктор" через кнопку
        wait.until(EC.element_to_be_clickable(account_locators.constructor_button)).click()
        assert wait.until(EC.visibility_of_element_located(home_locators.buns_section))

    @pytest.mark.usefixtures('login')
    def test_go_to_constructor_from_profile_via_logo(self, create_driver, wait, home_locators, account_locators):

        # переходим в профиль по клику на "Личный кабинет"
        wait.until(EC.element_to_be_clickable(home_locators.account_link)).click()

        # переходим из личного кабинета в "Конструктор" через логотип Stellar Burgers
        wait.until(EC.element_to_be_clickable(account_locators.logo_button)).click()
        assert wait.until(EC.visibility_of_element_located(home_locators.buns_section))

    @pytest.mark.usefixtures('login')
    def test_logout_from_account(self, create_driver, wait, home_locators, account_locators, login_locators):

        # переходим в профиль по клику на "Личный кабинет"
        wait.until(EC.element_to_be_clickable(home_locators.account_link)).click()

        # выходим из аккаунта
        wait.until(EC.element_to_be_clickable(account_locators.logout_button)).click()
        assert wait.until(EC.element_to_be_clickable(login_locators.login_button))
