from selenium.webdriver.common.by import By


# ==================== ХЕДЕР / НАВИГАЦИЯ ====================

# Кнопка «Конструктор» (по тексту в <p>)
CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")

# Кнопка «Личный кабинет» (по тексту в <p>)
PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")

# Логотип (ссылка с классом active)
LOGO = (By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2")


# ==================== ГЛАВНАЯ СТРАНИЦА ====================

# Кнопка «Войти в аккаунт» (на главной)
LOGIN_MAIN_BUTTON = (By.XPATH, "//button[normalize-space()='Войти в аккаунт']")
# Кнопка «Оформить заказ»
CHECKOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")

# Заголовок «Соберите бургер»
MAIN_TITLE = (By.XPATH, "//h1[contains(text(),'Соберите бургер')]")


# ==================== ФОРМА ВХОДА ====================

# Поле Email
LOGIN_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")

# Поле Пароль
LOGIN_PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")

# Кнопка «Войти» на форме входа
LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Войти']")

# Ссылка «Зарегистрироваться» на форме входа
REGISTER_LINK_ON_LOGIN = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")

# Ссылка «Восстановить пароль»
FORGOT_PASSWORD_LINK = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")

# ==================== ФОРМА РЕГИСТРАЦИИ ====================

# Поле Имя
REGISTER_NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")

# Поле Email
REGISTER_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")

# Поле Пароль
REGISTER_PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")

# Кнопка «Зарегистрироваться»
REGISTER_BUTTON = (By.XPATH, "//button[normalize-space()='Зарегистрироваться']")

# Ссылка «Войти» на форме регистрации
LOGIN_LINK_ON_REGISTER = (By.XPATH, "//a[contains(@class,'Auth_link__1fOlj')]")

# Ошибка пароля
PASSWORD_ERROR_MESSAGE = (By.XPATH, "//p[text()='Некорректный пароль']")


# ==================== ФОРМА ВОССТАНОВЛЕНИЯ ====================

# Кнопка «Войти» на форме восстановления
LOGIN_BUTTON_ON_FORGOT = (By.XPATH, "//a[@class='Auth_link__1fOlj']")


# ==================== ЛИЧНЫЙ КАБИНЕТ ====================

# Кнопка «Выйти»
LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")


# ==================== КОНСТРУКТОР (ТАБЫ) ====================

# Таб «Булки»
BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")

# Таб «Соусы»
SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")

# Таб «Начинки»
FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")
