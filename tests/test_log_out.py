from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
from data import authorization


class TestLogOut:
    def test_log_out_click_on_exit_button_show_login_page(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_HEADER))
        driver.find_element(*Locators.EMAIL).send_keys(authorization.login)
        driver.find_element(*Locators.PASSWORD).send_keys(authorization.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_HEADER))
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(Locators.EXIT_BUTTON)).click()
        text = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.LOGIN_HEADER)).text
        assert text == 'Вход'
