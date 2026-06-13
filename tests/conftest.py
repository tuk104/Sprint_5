import pytest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


# ==================== ГЕНЕРАТОРЫ ====================

def generate_email():
    digits = ''.join(str(random.randint(0, 9)) for _ in range(3))
    return f"pavel_andreev_48_{digits}@yandex.ru"


def generate_password(min_length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=min_length))


def generate_name():
    names = ["Анна", "Иван", "Петр", "Мария", "Дмитрий", "Елена", "Алексей", "Ольга"]
    return random.choice(names)


# ==================== ФИКСТУРЫ ДЛЯ ДРАЙВЕРА ====================

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/")
    driver.maximize_window()
    yield driver
    driver.quit()


# ==================== ФИКСТУРЫ ДЛЯ ДАННЫХ ====================

@pytest.fixture
def new_user_data():
    return {
        "name": generate_name(),
        "email": generate_email(),
        "password": generate_password(8)
    }

@pytest.fixture
def existing_user_data():
    return {
        "name": "Павлуша",
        "email": "andreev_48@gmail.com",
        "password": "qwertyasdfgh"
    }

@pytest.fixture
def new_user_with_min_password():
    return {
        "name": generate_name(),
        "email": generate_email(),
        "password": generate_password(6)
    }


@pytest.fixture
def invalid_password_data():
    return {
        "name": generate_name(),
        "email": generate_email(),
        "password": generate_password(3)  # Короткий пароль
    }


@pytest.fixture
def empty_name_data():
    return {
        "name": "",
        "email": generate_email(),
        "password": generate_password(8)
    }


# ==================== ФИКСТУРЫ ДЛЯ РЕГИСТРАЦИИ ====================

@pytest.fixture
def registered_user(driver, new_user_data):
    driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(REGISTER_LINK_ON_LOGIN)
    ).click()
    
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(REGISTER_NAME_INPUT)
    )
    driver.find_element(*REGISTER_NAME_INPUT).send_keys(new_user_data["name"])
    driver.find_element(*REGISTER_EMAIL_INPUT).send_keys(new_user_data["email"])
    driver.find_element(*REGISTER_PASSWORD_INPUT).send_keys(new_user_data["password"])
    driver.find_element(*REGISTER_BUTTON).click()
    
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(LOGIN_BUTTON)
    )
    
    return new_user_data


@pytest.fixture
def authorized_user(driver, existing_user_data):
    driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
    
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(LOGIN_EMAIL_INPUT)
    )
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(existing_user_data["email"])
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(existing_user_data["password"])
    driver.find_element(*LOGIN_BUTTON).click()

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(CHECKOUT_BUTTON)
    )
    
    return existing_user_data