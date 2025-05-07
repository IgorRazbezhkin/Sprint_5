from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import email, password
from locators import Login, Registration


def test_login_button_enter_your_account_login_completed(driver):
    driver.find_element(*Login.login_to_your_account_button).click()

    driver.find_element(*Login.email_button_on_the_login_page).send_keys(email)
    driver.find_element(*Login.password_button_on_login_page).send_keys(password)
    driver.find_element(*Login.login_button_on_login_page).click()

    WebDriverWait(driver, 5).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

def test_login_button_personal_account_login_completed(driver):
    driver.find_element(*Registration.personal_account_button).click()

    driver.find_element(*Login.email_button_on_the_login_page).send_keys(email)
    driver.find_element(*Login.password_button_on_login_page).send_keys(password)
    driver.find_element(*Login.login_button_on_login_page).click()

    WebDriverWait(driver, 5).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

def test_login_button_in_registration_form_login_completed(driver):
    driver.find_element(*Registration.personal_account_button).click()
    driver.find_element(*Registration.register_button).click()
    driver.find_element(*Login.login_button_on_the_registration_and_password_recovery_page).click()

    driver.find_element(*Login.email_button_on_the_login_page).send_keys(email)
    driver.find_element(*Login.password_button_on_login_page).send_keys(password)
    driver.find_element(*Login.login_button_on_login_page).click()

    WebDriverWait(driver, 5).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

def test_login_button_in_password_recovery_form_login_completed(driver):
    driver.find_element(*Registration.personal_account_button).click()
    driver.find_element(*Login.recover_password_button).click()
    driver.find_element(*Login.login_button_on_the_registration_and_password_recovery_page).click()

    driver.find_element(*Login.email_button_on_the_login_page).send_keys(email)
    driver.find_element(*Login.password_button_on_login_page).send_keys(password)
    driver.find_element(*Login.login_button_on_login_page).click()

    WebDriverWait(driver, 5).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'