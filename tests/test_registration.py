from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators


class TestRegistration:
    def test_success_registration_six_symbols_show_login_page(self, registration, password):
        driver = registration
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        text = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.LOGIN_HEADER)).text
        assert text == 'Вход'

    def test_failed_registration_less_than_six_symbols_show_error_invalid_password(self, registration):
        driver = registration
        driver.find_element(*Locators.PASSWORD).send_keys('123')
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        text = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.ERROR_INVALID_PASSWORD)).text
        assert text == 'Некорректный пароль'
