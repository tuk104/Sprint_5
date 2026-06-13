from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from conftest import driver, new_user_data, invalid_password_data, empty_name_data


class TestRegistration:
    
    def test_successful_registration(self, driver, new_user_data):
        # Переход на страницу регистрации
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(REGISTER_LINK_ON_LOGIN)
        ).click()
        
        # Заполнение формы
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(REGISTER_NAME_INPUT)
        )
        driver.find_element(*REGISTER_NAME_INPUT).send_keys(new_user_data["name"])
        driver.find_element(*REGISTER_EMAIL_INPUT).send_keys(new_user_data["email"])
        driver.find_element(*REGISTER_PASSWORD_INPUT).send_keys(new_user_data["password"])
        driver.find_element(*REGISTER_BUTTON).click()
        
        # Проверка: перебросило на страницу входа
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LOGIN_BUTTON)
        )
        assert driver.find_element(*LOGIN_BUTTON).is_displayed()
    
    def test_registration_with_invalid_password(self, driver, invalid_password_data):
        # Переход на страницу регистрации
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(REGISTER_LINK_ON_LOGIN)
        ).click()
        
        # Заполнение формы с коротким паролем
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(REGISTER_NAME_INPUT)
        )
        driver.find_element(*REGISTER_NAME_INPUT).send_keys(invalid_password_data["name"])
        driver.find_element(*REGISTER_EMAIL_INPUT).send_keys(invalid_password_data["email"])
        driver.find_element(*REGISTER_PASSWORD_INPUT).send_keys(invalid_password_data["password"])
        driver.find_element(*REGISTER_BUTTON).click()
        
        # Проверка: появилась ошибка "Некорректный пароль"
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(PASSWORD_ERROR_MESSAGE)
        )
        error_message = driver.find_element(*PASSWORD_ERROR_MESSAGE).text
        assert error_message == "Некорректный пароль"
    
    def test_registration_with_empty_name(self, driver, empty_name_data):
        # Переход на страницу регистрации
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(REGISTER_LINK_ON_LOGIN)
        ).click()
        
        # Заполнение формы с пустым именем
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(REGISTER_NAME_INPUT)
        )
        driver.find_element(*REGISTER_NAME_INPUT).send_keys(empty_name_data["name"])
        driver.find_element(*REGISTER_EMAIL_INPUT).send_keys(empty_name_data["email"])
        driver.find_element(*REGISTER_PASSWORD_INPUT).send_keys(empty_name_data["password"])

        expected_url = driver.current_url
        driver.find_element(*REGISTER_BUTTON).click()
        current_url = driver.current_url
        
        assert expected_url == current_url