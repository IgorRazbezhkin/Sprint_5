from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import email, password
from locators import Login, Registration, ConstructorSection


def test_transition_by_clicking_personal_account_page_open(driver):
    driver.find_element(*Registration.personal_account_button).click()

    driver.find_element(*Login.email_button_on_the_login_page).send_keys(email)
    driver.find_element(*Login.password_button_on_login_page).send_keys(password)
    driver.find_element(*Login.login_button_on_login_page).click()

    driver.find_element(*Registration.personal_account_button).click()

    WebDriverWait(driver, 5).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

def test_click_on_constructor_page_opens(driver):
    driver.find_element(*Registration.personal_account_button).click()
    driver.find_element(*ConstructorSection.button_constructor).click()

    WebDriverWait(driver, 5).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

def test_go_to_the_filling_section_page_completed(driver):
    driver.find_element(*ConstructorSection.filling_section).click()
    assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(ConstructorSection.filling_meat_of_the_immortal_mollusks_protostomia))

def test_go_to_the_sauces_section_page_completed(driver):
    driver.find_element(*ConstructorSection.sauces_section).click()
    assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(ConstructorSection.sauce_spicy_x))

def test_go_to_the_buns_section_page_completed(driver):
    driver.find_element(*ConstructorSection.filling_section).click()
    driver.find_element(*ConstructorSection.bun_section).click()
    assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(ConstructorSection.bun_fluorescent_bun_r2_d3))

def test_transition_by_clicking_on_the_stellar_burgers_logo_completed(driver):
    driver.find_element(*Registration.personal_account_button).click()
    driver.find_element(*Login.logo).click()

    WebDriverWait(driver, 5).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'