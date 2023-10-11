import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators

class TestSwitchConstructor:

    @pytest.mark.parametrize('button', [Locators.CONSTRUCTOR_BUTTON, Locators.LOGO_STELLAR_BURGERS])
    def test_switch_constructor_click_on_button_show_constructor_page(self, driver, button):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_HEADER))
        driver.find_element(*button).click()
        text = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_HEADER)).text
        assert text == 'Конструктор'
