from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from locators import *
from conftest import driver


class TestConstructor:
    
    def test_switch_to_BUNS_TUB(self, driver):
        # Сначала переключаемся на другой таб, чтобы уйти от активного
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(SAUCES_TAB)
        ).click()
        
        # Затем кликаем на таб "Булки"
        driver.find_element(*BUNS_TAB).click()
        
        # Проверка: секция "Булки" отображается
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(BUNS_TAB)
        )
        assert driver.find_element(*BUNS_TAB_ACTIVE).is_displayed()
    
    def test_switch_to_sauces_section(self, driver):
        # Кликаем на таб "Соусы"
        driver.find_element(*SAUCES_TAB).click()
        
        # Проверка: секция "Соусы" отображается
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(SAUCES_TAB)
        )
        assert driver.find_element(*SAUCES_TAB_ACTIVE).is_displayed()
    
    def test_switch_to_fillings_section(self, driver):
        # Кликаем на таб "Начинки"
        driver.find_element(*FILLINGS_TAB).click()
        
        # Проверка: секция "Начинки" отображается
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(FILLINGS_TAB)
        )
        assert driver.find_element(*FILLINGS_TAB_ACTIVE).is_displayed()
