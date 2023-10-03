import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators


class TestSwitchSections:
    @pytest.mark.parametrize(
        'section, header, title',
        [
            [Locators.SAUCES_SECTION, Locators.SAUCES_HEADER, 'Соусы'],
            [Locators.FILLINGS_SECTION, Locators.FILLINGS_HEADER, 'Начинки'],
            [Locators.BREADS_SECTION, Locators.BREADS_HEADER, 'Булки']
        ]
    )
    def test_switch_sections_click_on_sections_scrolling_to_sections(self, driver, section, header, title):
        driver.find_element(*section).click()
        text = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(header)).text
        assert text == title
