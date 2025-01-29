from selenium.webdriver.common.by import By

class BasePageLocators:
    YANDEX_LINK = (By.XPATH, ".//img[@alt = 'Yandex']")
    SCOOTER_LINK = (By.XPATH, ".//img[@alt = 'Scooter']")
    ORDER_BUTTON_TOP = (By.CLASS_NAME, 'Button_Button__ra12g')
    STATUS_ORDER_BUTTON = (By.XPATH, ".//*[text()='Статус заказа']")
    STATUS_ORDER_FIELD = (By.XPATH, ".//input[@placeholder='Введите номер заказа']")
    CHECK_STATUS_ORDER_BUTTON = (By.XPATH, ".//*[text()='Go!']")

