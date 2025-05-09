from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import email, password
from locators import Login, Registration


def test_exit_from_your_personal_account_by_pressing_the_button_completed(driver):
    driver.find_element(*Login.login_to_your_account_button).click()

    driver.find_element(*Login.email_button_on_the_login_page).send_keys(email)
    driver.find_element(*Login.password_button_on_login_page).send_keys(password)
    driver.find_element(*Login.login_button_on_login_page).click()

    driver.find_element(*Registration.personal_account_button).click()
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Login.logout_button)).click()

    WebDriverWait(driver, 5).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/login'))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'