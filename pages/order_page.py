import allure
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class OrderPage(BasePage):
    #driver = None
    first_name_field=[*OrderPageLocators.FIRST_NAME_FIELD]
    last_name_field=[*OrderPageLocators.LAST_NAME_FIELD]
    address_field=[*OrderPageLocators.ADDRESS_FIELD]
    station_field=[*OrderPageLocators.STATION_FIELD]
    station_field_value_alekseevskaya=[*OrderPageLocators.STATION_FIELD_VALUE_ALEKSEEVSKAYA]
    station_field_value_university=[*OrderPageLocators.STATION_FIELD_VALUE_UNIVERSITY]
    phone_field=[*OrderPageLocators.PHONE_FIELD]
    next_button=[*OrderPageLocators.NEXT_BUTTON]
    delivery_date_calendar=[*OrderPageLocators.DELIVERY_DATE_CALENDAR]
    time_rent_field=[*OrderPageLocators.TIME_RENT_FIELD]
    time_rent_field_value_two_days=[*OrderPageLocators.TIME_RENT_FIELD_VALUE_TWO_DAYS]
    time_rent_field_value_one_day=[*OrderPageLocators.TIME_RENT_FIELD_VALUE_ONE_DAY]
    black_pearl_checkbox=[*OrderPageLocators.BLACK_PEARL_CHECKBOX]
    gray_hopelessness_checkbox=[*OrderPageLocators.GRAY_HOPELESSNESS_CHECKBOX]
    comment_field=[*OrderPageLocators.COMMENT_FIELD]
    order_button=[*OrderPageLocators.ORDER_BUTTON_MIDDLE]
    accept_order_button=[*OrderPageLocators.ACCEPT_ORDER_BUTTON]
    number_order_label=[*OrderPageLocators.NUMBER_ORDER_LABEL]
    check_status_button=[*OrderPageLocators.CHECK_STATUS_BUTTON]

    @allure.step('Кликаем по полю Имя')
    def select_first_name_field(self):
        order_page = OrderPage(self.driver)
        order_page.click_on_element(*self.first_name_field)
    @allure.step('Заполняем поле Имя')
    def set_first_name(self, first_name):
        order_page = OrderPage(self.driver)
        order_page.set_in_element(*self.first_name_field, value=first_name)
    @allure.step('Кликаем по полю Фамилия')
    def select_last_name_field(self):
        order_page = OrderPage(self.driver)
        order_page.click_on_element(*self.last_name_field)
    @allure.step('Заполняем поле Фамилия')
    def set_last_name_fieldd(self, last_name):
        order_page = OrderPage(self.driver)
        order_page.set_in_element(*self.last_name_field, value=last_name)
    @allure.step('Кликаем по полю Адрес')
    def select_address_field(self):
        order_page = OrderPage(self.driver)
        order_page.click_on_element(*self.address_field)
    @allure.step('Заполняем поле Адрес')
    def set_address_field(self, address):
        order_page = OrderPage(self.driver)
        order_page.set_in_element(*self.address_field, value=address)
    @allure.step('Кликаем по полю Станция')
    def select_station_field(self):
        order_page = OrderPage(self.driver)
        order_page.click_on_element(*self.station_field)
    @allure.step('Выбираем среди значений поля Станция значение Алексеевская')
    def set_station_field_value_alekseevskaya(self):
        order_page = OrderPage(self.driver)
        order_page.scroll_to_element(*self.station_field_value_alekseevskaya)
        order_page.click_on_element(*self.station_field_value_alekseevskaya)
    @allure.step('Выбираем среди значений поля Станция значение Университет')
    def set_station_field_value_university(self):
        order_page = OrderPage(self.driver)
        order_page.scroll_to_element(*self.station_field_value_university)
        order_page.click_on_element(*self.station_field_value_university)
    @allure.step('Кликаем по полю Телефон')
    def select_phone_field(self):
        order_page = OrderPage(self.driver)
        order_page.click_on_element(*self.phone_field)
    @allure.step('Заполняем поле Телефон')
    def set_phone_field(self, phone_number):
        order_page = OrderPage(self.driver)
        order_page.set_in_element(*self.phone_field, value=phone_number)
    @allure.step('Кликаем по кнопке Далее')
    def select_next_button(self):
        order_page = OrderPage(self.driver)
        order_page.click_on_element(*self.next_button)
    @allure.step('Кликаем по полю Когда привезти самокат')
    def select_delivery_date_calendar(self):
        order_page = OrderPage(self.driver)
        order_page.click_on_element(*self.delivery_date_calendar)
    @allure.step('Заполняем поле Когда привезти самокат')
    def set_delivery_date_calendar(self, date):
        order_page = OrderPage(self.driver)
        order_page.set_in_element(*self.delivery_date_calendar, value=date)
        order_page.set_in_element(*self.delivery_date_calendar, value=Keys.ENTER)
    @allure.step('Кликаем по полю Срок аренды')
    def select_time_rent_field(self):
        order_page = OrderPage(self.driver)
        order_page.click_on_element(*self.time_rent_field)
    @allure.step('Выбираем среди значений выпадающего списка Срок аренды значение 2 дня')
    def select_time_rent_field_value_two_days(self):
        order_page = OrderPage(self.driver)
        order_page.click_on_element(*self.time_rent_field_value_two_days)
    @allure.step('Выбираем среди значений выпадающего списка Срок аренды значение 1 день')
    def select_time_rent_field_value_one_day(self):
        order_page = OrderPage(self.driver)
        order_page.click_on_element(*self.time_rent_field_value_one_day)
    @allure.step('Нажимаем на чекбокс Черный жемчуг')
    def set_black_pearl_checkbox(self):
        order_page = OrderPage(self.driver)
        order_page.click_on_element(*self.black_pearl_checkbox)
    @allure.step('Кликаем на чекбокс Серая безысходность')
    def set_gray_hopelessness_checkbox(self):
        order_page = OrderPage(self.driver)
        order_page.click_on_element(*self.gray_hopelessness_checkbox)
    @allure.step('Кликаем на поле Комментарий')
    def select_comment_field(self):
        order_page = OrderPage(self.driver)
        order_page.click_on_element(*self.comment_field)
    @allure.step('Заполняем поле Комментарий')
    def set_comment_field(self, comment):
        order_page = OrderPage(self.driver)
        order_page.set_in_element(*self.comment_field, value=comment)
    @allure.step('Кликаем на кнопку заказать')
    def select_order_button(self):
        order_page = OrderPage(self.driver)
        order_page.click_on_element(*self.order_button)
    @allure.step('Кликаем на кнопку подтверждения заказа')
    def select_accept_order_button(self):
        order_page = OrderPage(self.driver)
        order_page.wait_element_to_be_clickable(*self.accept_order_button)
        order_page.click_on_element(*self.accept_order_button)
    @allure.step('Получаем номер заказа')
    def get_order_number(self):
        order_page = OrderPage(self.driver)
        order_number = order_page.get_text_element(*self.number_order_label)
        return order_number
    @allure.step('Кликаем на кнопку просмотра статуса заказа')
    def select_check_status_button(self):
        order_page = OrderPage(self.driver)
        order_page.click_on_element(*self.check_status_button)
