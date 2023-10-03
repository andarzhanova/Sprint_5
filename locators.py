from selenium.webdriver.common.by import By


class Locators:
    PERSONAL_ACCOUNT_BUTTON = (By.LINK_TEXT, 'Личный Кабинет')  # Кнопка "Личный кабинет"
    LOGIN_HEADER = (By.XPATH, '.// h2[text() = "Вход"]')  # Заголовок "Вход"
    REGISTER_LINK = (By.LINK_TEXT, 'Зарегистрироваться')  # Ссылка "Зарегистрироваться"
    REGISTRATION_HEADER = (By.XPATH, '.// h2[text() = "Регистрация"]')  # Заголовок "Регистрация"
    NAME = (By.XPATH, './/div[label[text()="Имя"]]/input')  # Поле для имени
    EMAIL = (By.XPATH, './/div[label[text()="Email"]]/input')  # Поле для email
    PASSWORD = (By.NAME, 'Пароль')  # Поле для пароля
    REGISTER_BUTTON = (By.XPATH, '//button[(text()="Зарегистрироваться")]')  # Кнопка "Зарегистрироваться"
    ERROR_INVALID_PASSWORD = (By.XPATH, '//p[(text()="Некорректный пароль")]')  # Ошибка некорректный пароль
    LOG_IN_TO_ACCOUNT_BUTTON = (By.XPATH, '//button[(text()="Войти в аккаунт")]')  # Кнопка "Войти в аккаунт"
    LOGIN_BUTTON = (By.XPATH, '//button[(text()="Войти")]')  # Кнопка "Войти"
    CONSTRUCTOR_HEADER = (By.LINK_TEXT, 'Конструктор')  # Заголовок "Конструктор"
    LOGIN_LINK = (By.LINK_TEXT, 'Войти')  # Ссылка "Войти"
    RESTORE_PASSWORD_LINK = (By.LINK_TEXT, 'Восстановить пароль')  # Ссылка "Восстановить пароль"
    PASSWORD_RECOVERY_HEADER = (By.XPATH,
                                './/h2[text() = "Восстановление пароля"]')  # Заголовок "Восстановление пароля"
    CONSTRUCTOR_BUTTON = (By.LINK_TEXT, 'Конструктор')  # Кнопка "Конструктор"
    LOGO_STELLAR_BURGERS = (By.XPATH, '//nav/div/a')  # Логотип Stellar Burgers
    EXIT_BUTTON = (By.XPATH, '//button[(text()="Выход")]')  # Кнопка "Выход"
    SAUCES_SECTION = (By.XPATH, '//span[(text()="Соусы")]')  # Раздел "Соусы"
    SAUCES_HEADER = (By.XPATH, '//h2[(text()="Соусы")]')  # Заголовок "Соусы"
    FILLINGS_SECTION = (By.XPATH, '//span[(text()="Начинки")]')  # Раздел "Начинки"
    FILLINGS_HEADER = (By.XPATH, '//h2[(text()="Начинки")]')  # Заголовок "Начинки"
    BREADS_SECTION = (By.XPATH, '//span[(text()="Начинки")]')  # Раздел "Булки"
    BREADS_HEADER = (By.XPATH, '//h2[(text()="Булки")]')  # Заголовок "Булки"
