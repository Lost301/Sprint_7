import allure
import requests

from constants import BASE_URL
from helpers import generate_random_string


@allure.epic('Courier')
class TestCreateCourier:
    @allure.title('Курьера можно создать, передав все обязательные поля')
    @allure.description('Проверяем, что запрос с логином, паролем и именем возвращает 201 и {"ok": true}')
    def test_create_courier_all_required_fields_created(self):
        payload = {
            'login': generate_random_string(10),
            'password': generate_random_string(10),
            'firstName': generate_random_string(10),
        }
        response = requests.post(f'{BASE_URL}/courier', data=payload)
        assert response.status_code == 201
        assert response.json() == {'ok': True}

    @allure.title('Нельзя создать двух курьеров с одинаковым логином')
    @allure.description('Проверяем, что повторная регистрация с тем же логином возвращает 409')
    def test_create_courier_duplicate_login_conflict(self, courier_credentials):
        payload = {
            'login': courier_credentials[0],
            'password': generate_random_string(10),
            'firstName': generate_random_string(10),
        }
        response = requests.post(f'{BASE_URL}/courier', data=payload)
        assert response.status_code == 409
        assert 'Этот логин уже используется' in response.json()['message']

    @allure.title('Нельзя создать курьера без логина')
    @allure.description('Проверяем, что запрос без поля login возвращает 400')
    def test_create_courier_without_login_bad_request(self):
        payload = {
            'password': generate_random_string(10),
            'firstName': generate_random_string(10),
        }
        response = requests.post(f'{BASE_URL}/courier', data=payload)
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'

    @allure.title('Нельзя создать курьера без пароля')
    @allure.description('Проверяем, что запрос без поля password возвращает 400')
    def test_create_courier_without_password_bad_request(self):
        payload = {
            'login': generate_random_string(10),
            'firstName': generate_random_string(10),
        }
        response = requests.post(f'{BASE_URL}/courier', data=payload)
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'
