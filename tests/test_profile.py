from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from conftest import driver, authorized_user


class TestProfile:
    
    def test_go_to_personal_account(self, driver, authorized_user):
        # Кликаем «Личный кабинет»
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        
        # Проверка: попали в личный кабинет (видно кнопку "Выйти")
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LOGOUT_BUTTON)
        )
        assert driver.find_element(*LOGOUT_BUTTON).is_displayed()
    
    def test_go_from_profile_to_constructor_via_button(self, driver, authorized_user):
        # Переход в личный кабинет
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LOGOUT_BUTTON)
        )
        
        # Кликаем «Конструктор»
        driver.find_element(*CONSTRUCTOR_BUTTON).click()
        
        # Проверка: вернулись на главную (видим заголовок)
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MAIN_TITLE)
        )
        assert driver.find_element(*MAIN_TITLE).is_displayed()
    
    def test_go_from_profile_to_main_via_logo(self, driver, authorized_user):
        # Переход в личный кабинет
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LOGOUT_BUTTON)
        )
        
        # Кликаем на логотип
        driver.find_element(*LOGO).click()
        
        # Проверка: вернулись на главную (видим заголовок)
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MAIN_TITLE)
        )
        assert driver.find_element(*MAIN_TITLE).is_displayed()