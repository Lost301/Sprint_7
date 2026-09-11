import allure
import requests

from helpers import BASE_URL


@allure.epic('Orders')
class TestOrdersList:
    @allure.title('В ответе на запрос списка заказов возвращается список заказов')
    @allure.description('Проверяем, что GET /orders возвращает 200 и ключ orders со списком в теле')
    def test_get_orders_list_no_params_success(self):
        response = requests.get(f'{BASE_URL}/orders')
        assert response.status_code == 200
        assert isinstance(response.json().get('orders'), list)
