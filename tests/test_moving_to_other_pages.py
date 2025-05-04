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

def test_transition_by_clicking_personal_account_page_open():
    driver.find_element(By.XPATH, ".//*[@href='/account']").click()

    driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys(email)
    driver.find_element(By.XPATH, ".//label[text()='Пароль']/following-sibling::input").send_keys(password)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

    driver.find_element(By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]").click()

    WebDriverWait(driver, 5).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

def test_click_on_constructor_page_opens():
    driver.find_element(By.XPATH, ".//p[text()='Конструктор']").click()

    WebDriverWait(driver, 5).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

    assert current_url == 'https://stellarburgers.nomoreparties.site/'

def test_go_to_the_filling_section_page_completed():
    driver.find_element(By.XPATH, ".//span[text()='Начинки']").click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//p[text()='Мясо бессмертных моллюсков Protostomia']")))

def test_go_to_the_sauces_section_page_completed():
    driver.find_element(By.XPATH, ".//span[text()='Соусы']").click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//p[text()='Соус Spicy-X']")))

def test_go_to_the_buns_section_page_completed():
    driver.find_element(By.XPATH, ".//span[text()='Булки']").click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3']")))

def test_transition_by_clicking_on_the_stellar_burgers_logo_completed():
    driver.find_element(By.XPATH, ".//*[@href='/account']").click()
    driver.find_element(By.CLASS_NAME, "AppHeader_header__logo__2D0X2").click()

    WebDriverWait(driver, 5).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

    assert current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.quit()