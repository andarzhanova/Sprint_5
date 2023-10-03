import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators


class TestLogin:

    @pytest.mark.parametrize('button', [Locators.LOG_IN_TO_ACCOUNT_BUTTON, Locators.PERSONAL_ACCOUNT_BUTTON])
    def test_login_click_on_button_show_constructor_page(self, driver, button):
        driver.find_element(*button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_HEADER))
        driver.find_element(*Locators.EMAIL).send_keys('annaandarzhanova1123@yandex.ru')
        driver.find_element(*Locators.PASSWORD).send_keys('963258')
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        text = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_HEADER)).text
        assert text == 'Конструктор'

    @pytest.mark.parametrize(
        'link, header',
        [
            [Locators.REGISTER_LINK, Locators.REGISTRATION_HEADER],
            [Locators.RESTORE_PASSWORD_LINK, Locators.PASSWORD_RECOVERY_HEADER]
        ]
    )
    def test_login_click_on_link_show_constructor_page(self, driver, link, header):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_HEADER))
        driver.find_element(*link).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(header))
        driver.find_element(*Locators.LOGIN_LINK).click()
        driver.find_element(*Locators.EMAIL).send_keys('annaandarzhanova1123@yandex.ru')
        driver.find_element(*Locators.PASSWORD).send_keys('963258')
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        text = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_HEADER)).text
        assert text == 'Конструктор'
