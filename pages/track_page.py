import allure
from locators.track_page_locators import TrackPageLocators
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage


class TrackPage(BasePage):
    driver = None
    check_status_order_button = [*TrackPageLocators.CHECK_STATUS_ORDER_BUTTON]
    yandex_link = [*BasePageLocators.YANDEX_LINK]
    scooter_link = [*BasePageLocators.SCOOTER_LINK]

    @allure.step('Кликаем по кнопке проверить статус заказа')
    def select_check_status_order_button(self):
        main_page = TrackPage(self.driver)
        main_page.click_on_element_by_xpath(*self.check_status_order_button)

    @allure.step('Кликаем по ссылке на страницу Яндекс Дзена')
    def select_yandex_link(self):
        main_page = TrackPage(self.driver)
        main_page.click_on_element_by_xpath(*self.yandex_link)

    @allure.step('Кликаем по ссылке на главную страницу')
    def select_scooter_link(self):
        main_page = TrackPage(self.driver)
        main_page.click_on_element_by_xpath(*self.scooter_link)
