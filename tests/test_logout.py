from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from conftest import driver, authorized_user


class TestLogout:
    
    def test_logout_from_account(self, driver, authorized_user):

        # Переход в личный кабинет
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        
        # Кликаем «Выйти»
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(LOGOUT_BUTTON)
        ).click()
        
        # Проверка: вышли из аккаунта (появилась кнопка «Войти»)
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LOGIN_BUTTON)
        )
        assert driver.find_element(*LOGIN_BUTTON).is_displayed()