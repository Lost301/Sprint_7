import allure
import requests

from helpers import BASE_URL


@allure.epic('Orders')
class TestAcceptOrder:
    @allure.title('Заказ можно принять, передав id заказа и id курьера')
    @allure.description('Проверяем, что успешный запрос возвращает 200 и {"ok": true}')
    def test_accept_order_valid_ids_accepted(self, order_track, courier_id):
        order_id = self._get_order_id(order_track)
        response = requests.put(f'{BASE_URL}/orders/accept/{order_id}', params={'courierId': courier_id})
        assert response.status_code == 200
        assert response.json() == {'ok': True}

    @allure.title('Нельзя принять заказ без id курьера')
    @allure.description('Проверяем, что запрос без параметра courierId возвращает 400')
    def test_accept_order_no_courier_id_bad_request(self, order_track):
        order_id = self._get_order_id(order_track)
        response = requests.put(f'{BASE_URL}/orders/accept/{order_id}')
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для поиска'

    @allure.title('Нельзя принять заказ с несуществующим id курьера')
    @allure.description('Проверяем, что запрос с неверным courierId возвращает 404')
    def test_accept_order_nonexistent_courier_id_not_found(self, order_track):
        order_id = self._get_order_id(order_track)
        response = requests.put(f'{BASE_URL}/orders/accept/{order_id}', params={'courierId': 999999999})
        assert response.status_code == 404
        assert response.json()['message'] == 'Курьера с таким id не существует'

    @allure.title('Нельзя принять заказ без id заказа')
    @allure.description('Проверяем, что запрос без id заказа в пути возвращает 404')
    def test_accept_order_no_order_id_not_found(self, courier_id):
        response = requests.put(f'{BASE_URL}/orders/accept/', params={'courierId': courier_id})
        assert response.status_code == 404

    @allure.title('Нельзя принять заказ с несуществующим id заказа')
    @allure.description('Проверяем, что запрос с неверным id заказа возвращает 404')
    def test_accept_order_nonexistent_order_id_not_found(self, courier_id):
        response = requests.put(f'{BASE_URL}/orders/accept/999999999', params={'courierId': courier_id})
        assert response.status_code == 404
        assert response.json()['message'] == 'Заказа с таким id не существует'

    @staticmethod
    @allure.step('Получаем id заказа по треку {track}')
    def _get_order_id(track):
        response = requests.get(f'{BASE_URL}/orders/track', params={'t': track})
        return response.json()['order']['id']
