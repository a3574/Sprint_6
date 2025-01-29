import allure
import pytest
from pages.main_page import MainPage
from helpers import UserData

class TestQuestion:
    @allure.title('Вопросы о важном')
    @allure.description('Проверяем раздел Вопросы о важном в отдельном теcте. Проверяем соответствие каждого вопроса своему ответу занеенного в helpers в словаре test_data_for_tests_question')
    @pytest.mark.parametrize("data", UserData.get_test_data_for_tests_question())
    def test_question_for_differrent_data_check_answer(self, data):
        main_page = MainPage(self.driver)
        main_page.open_main_page()
        answer = main_page.get_answer_by_question(data['question'])
        assert answer == data['answer']
