import allure
from locators.track_page_locators import TrackPageLocators
from locators.base_page_locators import BasePageLocators
class TrackPage():
    driver = None
    check_status_order_button=[*TrackPageLocators.CHECK_STATUS_ORDER_BUTTON]
    yandex_link=[*BasePageLocators.YANDEX_LINK]
    scooter_link=[*BasePageLocators.SCOOTER_LINK]

    def __init__(self, driver):
        self.driver = driver
    @allure.step('Кликаем по кнопке проверить статус заказа')
    def select_check_status_order_button(self):
        element = self.driver.find_element(*self.check_status_order_button)
        element.click()
    @allure.step('Кликаем по ссылке на страницу Яндекс Дзена')
    def select_yandex_link(self):
        element = self.driver.find_element(*self.yandex_link)
        element.click()
    @allure.step('Кликаем по ссылке на главную страницу')
    def select_scooter_link(self):
        element = self.driver.find_element(*self.scooter_link)
        element.click()