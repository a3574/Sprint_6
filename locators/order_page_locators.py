from selenium.webdriver.common.by import By


class OrderPageLocators:
    FIRST_NAME_FIELD = (By.XPATH, ".//input[@placeholder = '* Имя']")
    LAST_NAME_FIELD = (By.XPATH, ".//input[@placeholder = '* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, ".//input[@placeholder = '* Адрес: куда привезти заказ']")
    STATION_FIELD = (By.XPATH, ".//input[@placeholder = '* Станция метро']")
    STATION_FIELD_VALUE_ALEKSEEVSKAYA = (By.XPATH, ".//*[text()='Алексеевская']")
    STATION_FIELD_VALUE_UNIVERSITY = (By.XPATH, ".//*[text()='Университет']")
    PHONE_FIELD = (By.XPATH, ".//input[@placeholder = '* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")
    DELIVERY_DATE_CALENDAR = (By.XPATH, ".//input[@placeholder = '* Когда привезти самокат']")
    TIME_RENT_FIELD = (By.XPATH, ".//*[text()='* Срок аренды']")
    TIME_RENT_FIELD_VALUE_TWO_DAYS = (By.XPATH, ".//*[text()='двое суток']")
    TIME_RENT_FIELD_VALUE_ONE_DAY = (By.XPATH, ".//*[text()='сутки']")
    BLACK_PEARL_CHECKBOX = (By.XPATH, ".//*[text() = 'чёрный жемчуг']")
    GRAY_HOPELESSNESS_CHECKBOX = (By.XPATH, ".//*[text() = 'серая безысходность']")
    COMMENT_FIELD = (By.XPATH, ".//*[@placeholder = 'Комментарий для курьера']")
    ORDER_BUTTON_MIDDLE = (By.XPATH, ".//button[@class ='Button_Button__ra12g Button_Middle__1CSJM']")
    ACCEPT_ORDER_BUTTON = (By.XPATH, ".//*[text()='Да']")
    CHECK_STATUS_BUTTON = (By.XPATH, ".//*[text()='Посмотреть статус']")
    NUMBER_ORDER_LABEL = (By.CLASS_NAME, 'Order_Text__2broi')
