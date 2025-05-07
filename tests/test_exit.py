from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import email, password


def test_exit_from_your_personal_account_by_pressing_the_button_completed(driver):
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()

    driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys(email)
    driver.find_element(By.XPATH, ".//label[text()='Пароль']/following-sibling::input").send_keys(password)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

    driver.find_element(By.XPATH, ".//*[@href='/account']").click()
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//button[contains(text(), 'Выход')]"))).click()

    WebDriverWait(driver, 10).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/login'))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    driver.quit()