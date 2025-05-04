from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import random_name, random_email


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://stellarburgers.nomoreparties.site/")

valid_password = '123456'
invalid_password = '123'

def test_registration_completed(random_name, random_email):
    driver.find_element(By.XPATH, ".//*[@href='/account']").click()
    driver.find_element(By.XPATH, ".//*[@href='/register']").click()

    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, ".//label[text()='Имя']")))

    driver.find_element(By.XPATH, ".//label[text()='Имя']/following-sibling::input").send_keys(random_name)
    driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys(random_email)
    driver.find_element(By.XPATH, ".//label[text()='Пароль']/following-sibling::input").send_keys(valid_password)

    driver.find_element(By.XPATH, ".//button[contains(text(), 'Зарегистрироваться')]").click()

    WebDriverWait(driver, 5).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/login'))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

def test_registration_with_invalid_password_error_incorrect_password(random_email, random_name):
    driver.find_element(By.XPATH, ".//*[@href='/account']").click()
    driver.find_element(By.XPATH, ".//*[@href='/register']").click()

    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, ".//label[text()='Имя']")))

    driver.find_element(By.XPATH, ".//label[text()='Имя']/following-sibling::input").send_keys(random_name)
    driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys(random_email)
    driver.find_element(By.XPATH, ".//label[text()='Пароль']/following-sibling::input").send_keys(invalid_password)

    driver.find_element(By.XPATH, ".//button[contains(text(), 'Зарегистрироваться')]").click()

    error_message = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//p[contains(text(), 'Некорректный пароль')]")))

    assert error_message is not None

    driver.quit()