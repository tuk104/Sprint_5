from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from conftest import driver, registered_user
from data import *


class TestLogin:
    
    def test_login_via_main_button(self, driver):
        
        # Клик по кнопке "Войти в аккаунт"
        driver.find_element(*LOGIN_MAIN_BUTTON).click()
        
        # Ввод данных
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LOGIN_EMAIL_INPUT)
        )
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(EXISTING_USER["email"])
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(EXISTING_USER["password"])
        driver.find_element(*LOGIN_BUTTON).click()
        
        # Проверка: после входа появилась кнопка "Оформить заказ"
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(CHECKOUT_BUTTON)
        )
        assert driver.find_element(*CHECKOUT_BUTTON).is_displayed()
    
    def test_login_via_personal_account_button(self, driver):
        # Клик по "Личный кабинет"
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        
        # Ввод данных
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LOGIN_EMAIL_INPUT)
        )
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(EXISTING_USER["email"])
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(EXISTING_USER["password"])
        driver.find_element(*LOGIN_BUTTON).click()
        
        # Проверка: успешный вход
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(CHECKOUT_BUTTON)
        )
        assert driver.find_element(*CHECKOUT_BUTTON).is_displayed()
    
    def test_login_via_register_form(self, driver):
        # Переход на страницу регистрации
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(REGISTER_LINK_ON_LOGIN)
        ).click()
        
        # На странице регистрации кликаем ссылку "Войти"
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(LOGIN_LINK_ON_REGISTER)
        ).click()
        
        # Ввод данных
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LOGIN_EMAIL_INPUT)
        )
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(EXISTING_USER["email"])
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(EXISTING_USER["password"])
        driver.find_element(*LOGIN_BUTTON).click()
        
        # Проверка: успешный вход
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(CHECKOUT_BUTTON)
        )
        assert driver.find_element(*CHECKOUT_BUTTON).is_displayed()
    
    def test_login_via_forgot_password_form(self, driver):
        # Переход на страницу восстановления пароля
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(FORGOT_PASSWORD_LINK)
        ).click()
        
        # На странице восстановления кликаем "Войти"
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(LOGIN_BUTTON_ON_FORGOT)
        ).click()
        
        # Ввод данных
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LOGIN_EMAIL_INPUT)
        )
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(EXISTING_USER["email"])
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(EXISTING_USER["password"])
        driver.find_element(*LOGIN_BUTTON).click()
        
        # Проверка: успешный вход
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(CHECKOUT_BUTTON)
        )
        assert driver.find_element(*CHECKOUT_BUTTON).is_displayed()