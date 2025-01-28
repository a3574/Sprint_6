import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.track_page import TrackPage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urls import Urls
from helpers import UserData
class TestOrder():
    @allure.title('Заказ самоката')
    @allure.description('Проверяем весь флоу позитивного сценария с двумя наборами данных. Проверяем по отдельности две точки входа в сценарий: кнопка «Заказать» вверху страницы и внизу. Проверяем: 1, что появилось всплывающее окно с сообщением об успешном создании заказа; 2 что если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката»; 3 что если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена. На вход теста подаются 2 набора данных через параметризацию')
    @pytest.mark.parametrize("data", UserData.get_test_data_for_tests_order())
    def test_order_with_two_different_entry_order_has_been_placed(self, data):
        main_page = MainPage(self.driver)
        order_page = OrderPage(self.driver)
        track_page = TrackPage(self.driver)
        order_number = ''
        check_move_main_page = ''
        check_move_dzen_page = ''
        # Открываем главную страницу
        main_page.open_main_page()

        # Нажимаем кнопку заказа
        if data['order_button'] == 'top':
            main_page.click_order_button_top()
        elif data['order_button'] == 'middle':
            main_page.click_order_button_middle()

        # Заполняем поле "Имя"
        order_page.select_first_name_field()
        order_page.set_first_name(data['first_name'])

        # Заполняем поле "Фамилия"
        order_page.select_last_name_field()
        order_page.set_last_name_fieldd(data['last_name'])

        # Заполняем поле "Адрес"
        order_page.select_address_field()
        order_page.set_address_field(data['address'])

        # Выбираем станцию
        order_page.select_station_field()
        if data['station'] == 'Алексеевская':
            order_page.set_station_field_value_alekseevskaya()
        elif data['station'] == 'Университет':
            order_page.set_station_field_value_university()

        # Заполняем поле телефонного номера
        order_page.select_phone_field()
        order_page.set_phone_field(data['phone_number'])

        # Нажимаю на кнопку далее
        order_page.select_next_button()

        # Заполняем дату доставки
        order_page.select_delivery_date_calendar()
        order_page.set_delivery_date_calendar(data['delivery_date'])

        # Заполняем срок аренды
        order_page.select_time_rent_field()
        if data['time_rent'] == 'one':
            order_page.select_time_rent_field_value_one_day()
        elif data['time_rent'] == 'two':
            order_page.select_time_rent_field_value_two_days()

        # Выбираем цвет
        if data['color'] == 'black_pearl':
            order_page.set_black_pearl_checkbox()
        elif data['color'] == 'gray_hopelessness':
            order_page.set_gray_hopelessness_checkbox()

        # Оставляем комментарий
        order_page.select_comment_field()
        order_page.set_comment_field(data['comment'])

        # Нажимаем "Заказать"
        order_page.select_order_button()

        # Нажимаем "Да"
        order_page.select_accept_order_button()

        # Получаем номер заказа и соответственно выполняем задание "Проверить, что появилось всплывающее окно с сообщением об успешном создании заказа."
        order_number = order_page.get_order_number()

        # Переходим на форму проверки заказа
        order_page.select_check_status_button()

        # Переходим на главную страницу
        track_page.select_scooter_link()
        WebDriverWait(self.driver, 15).until(expected_conditions.url_changes(Urls.main_page))
        if self.driver.current_url == Urls.main_page_directory:
            check_move_main_page = '1'

        # Переходим на страницу заказа
        main_page.select_status_order_button()
        main_page.set_status_order_field(order_number)
        main_page.select_check_status_order_button()

        # Переходим на страницу Дзена
        track_page.select_yandex_link()
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 15).until(expected_conditions.title_contains('Дзен'))
        if self.driver.current_url == Urls.dzen_page:
            check_move_dzen_page = '1'

        # Проверяем, что удалось завести заказ(есть номер заказа), что был переход с формы отслеживания заказа как на главную страницу, так и на страницу дзена.
        assert check_move_dzen_page == '1' and check_move_main_page == '1' and order_number != ''
