import pytest
import random
from faker import Faker
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators

faker = Faker()


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1200,600')
    browser = webdriver.Chrome(options=chrome_options)
    browser.get("https://stellarburgers.nomoreparties.site/")

    yield browser
    browser.quit()


@pytest.fixture
def login():
    name_surname = faker.name().replace(' ', '')
    num = str(random.randint(1000, 1999))
    domain = faker.free_email().split('@')[1]
    login = name_surname + num + '@' + domain
    return login


@pytest.fixture
def password():
    password = ''
    while len(password) < 6:
        password += str(random.randint(0, 9))
    return password


@pytest.fixture
def registration(driver, login):
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_HEADER))
    driver.find_element(*Locators.REGISTER_LINK).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION_HEADER))
    driver.find_element(*Locators.NAME).send_keys('Anna')
    driver.find_element(*Locators.EMAIL).send_keys(login)
    return driver
