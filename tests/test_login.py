from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://stellarburgers.nomoreparties.site/")

email = 'Igor_Razbezhkin_19_495@gmail.ru'
password = '2900405'
current_url = driver.current_url

def test_login_button_enter_your_account_login_completed():
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()

    driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys(email)
    driver.find_element(By.XPATH, ".//label[text()='Пароль']/following-sibling::input").send_keys(password)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

    WebDriverWait(driver, 5).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

    assert current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.find_element(By.XPATH, ".//*[@href='/account']").click()

    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//button[contains(text(), 'Выход')]"))).click()

def test_login_button_personal_account_login_completed():
    driver.find_element(By.XPATH, ".//*[@href='/account']").click()

    driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys(email)
    driver.find_element(By.XPATH, ".//label[text()='Пароль']/following-sibling::input").send_keys(password)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

    WebDriverWait(driver, 5).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

    assert current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.find_element(By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]").click()

    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//button[contains(text(), 'Выход')]"))).click()

def test_login_button_in_registration_form_login_completed():
    driver.find_element(By.XPATH, ".//*[@href='/account']").click()
    driver.find_element(By.XPATH, ".//*[@href='/register']").click()
    driver.find_element(By.XPATH, ".//*[@href='/login']").click()

    driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys(email)
    driver.find_element(By.XPATH, ".//label[text()='Пароль']/following-sibling::input").send_keys(password)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

    WebDriverWait(driver, 5).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

    assert current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.find_element(By.XPATH, ".//*[@href='/account']").click()

    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//button[contains(text(), 'Выход')]"))).click()


def test_login_button_in_password_recovery_form_login_completed():
    driver.find_element(By.XPATH, ".//*[@href='/account']").click()
    driver.find_element(By.XPATH, ".//*[@href='/forgot-password']").click()
    driver.find_element(By.XPATH, ".//*[@href='/login']").click()

    driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys(email)
    driver.find_element(By.XPATH, ".//label[text()='Пароль']/following-sibling::input").send_keys(password)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

    WebDriverWait(driver, 5).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

    assert current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.quit()