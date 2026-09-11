import allure
import requests

from helpers import BASE_URL


@allure.epic('Orders')
class TestGetOrderByTrack:
    @allure.title('По трек-номеру можно получить заказ')
    @allure.description('Проверяем, что успешный запрос возвращает 200 и объект заказа с этим треком')
    def test_get_order_by_track_valid_track_success(self, order_track):
        response = requests.get(f'{BASE_URL}/orders/track', params={'t': order_track})
        assert response.status_code == 200
        assert response.json()['order']['track'] == order_track

    @allure.title('Запрос заказа без трек-номера возвращает ошибку')
    @allure.description('Проверяем, что запрос без параметра t возвращает 400')
    def test_get_order_by_track_no_track_bad_request(self):
        response = requests.get(f'{BASE_URL}/orders/track')
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для поиска'

    @allure.title('Запрос заказа с несуществующим трек-номером возвращает ошибку')
    @allure.description('Проверяем, что запрос с несуществующим треком возвращает 404')
    def test_get_order_by_track_nonexistent_track_not_found(self):
        response = requests.get(f'{BASE_URL}/orders/track', params={'t': 999999999})
        assert response.status_code == 404
        assert response.json()['message'] == 'Заказ не найден'
