import allure
import pytest
import requests

from constants import BASE_URL
from helpers import order_payload


@allure.epic('Orders')
class TestCreateOrder:
    @allure.title('Создание заказа с цветом: {colors}')
    @allure.description('Проверяем, что заказ создаётся с любым набором цветов и в ответе есть track')
    @pytest.mark.parametrize('colors', [['BLACK'], ['GREY'], ['BLACK', 'GREY'], None],
                             ids=['black', 'grey', 'black_and_grey', 'no_color'])
    def test_create_order_with_colors_track_created(self, colors, created_tracks):
        response = requests.post(f'{BASE_URL}/orders', json=order_payload(colors))
        created_tracks.append(response.json().get('track'))
        assert response.status_code == 201
        assert 'track' in response.json()
