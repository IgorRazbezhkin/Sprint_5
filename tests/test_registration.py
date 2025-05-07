from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers import random_name, random_email
from data import valid_password, invalid_password
from locators import Registration


def test_registration_completed(driver):
    name = random_name()
    email = random_email()

    driver.find_element(*Registration.personal_account_button).click()
    driver.find_element(*Registration.register_button).click()

    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(Registration.placeholder_name))

    driver.find_element(*Registration.field_name).send_keys(name)
    driver.find_element(*Registration.field_email).send_keys(email)
    driver.find_element(*Registration.field_password).send_keys(valid_password)

    driver.find_element(*Registration.button_to_complete_registration).click()

    WebDriverWait(driver, 5).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/login'))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

def test_registration_with_invalid_password_error_incorrect_password(driver):
    name = random_name()
    email = random_email()

    driver.find_element(*Registration.personal_account_button).click()
    driver.find_element(*Registration.register_button).click()

    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(Registration.placeholder_name))

    driver.find_element(*Registration.field_name).send_keys(name)
    driver.find_element(*Registration.field_email).send_keys(email)
    driver.find_element(*Registration.field_password).send_keys(invalid_password)

    driver.find_element(*Registration.button_to_complete_registration).click()

    error_message = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Registration.incorrect_password_error_message))

    assert error_message is not None