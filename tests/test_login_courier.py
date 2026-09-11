import allure
import requests

from helpers import BASE_URL, generate_random_string


@allure.epic('Courier')
class TestLoginCourier:
    @allure.title('Курьер может авторизоваться с валидными логином и паролем')
    @allure.description('Проверяем, что успешный логин возвращает 200 и id курьера в теле ответа')
    def test_login_courier_valid_credentials_success(self, courier_credentials):
        payload = {'login': courier_credentials[0], 'password': courier_credentials[1]}
        response = requests.post(f'{BASE_URL}/courier/login', data=payload)
        assert response.status_code == 200
        assert 'id' in response.json()

    @allure.title('Нельзя авторизоваться без логина')
    @allure.description('Проверяем, что запрос с пустым полем login возвращает 400')
    def test_login_courier_without_login_bad_request(self, courier_credentials):
        payload = {'login': '', 'password': courier_credentials[1]}
        response = requests.post(f'{BASE_URL}/courier/login', data=payload)
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для входа'

    @allure.title('Нельзя авторизоваться без пароля')
    @allure.description('Проверяем, что запрос с пустым полем password возвращает 400')
    def test_login_courier_without_password_bad_request(self, courier_credentials):
        payload = {'login': courier_credentials[0], 'password': ''}
        response = requests.post(f'{BASE_URL}/courier/login', data=payload)
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для входа'

    @allure.title('Система возвращает ошибку при неверном пароле')
    @allure.description('Проверяем, что логин с неправильным паролем возвращает 404')
    def test_login_courier_wrong_password_not_found(self, courier_credentials):
        payload = {'login': courier_credentials[0], 'password': generate_random_string(10)}
        response = requests.post(f'{BASE_URL}/courier/login', data=payload)
        assert response.status_code == 404
        assert response.json()['message'] == 'Учетная запись не найдена'

    @allure.title('Система возвращает ошибку при авторизации несуществующим пользователем')
    @allure.description('Проверяем, что логин с несуществующей парой логин-пароль возвращает 404')
    def test_login_courier_nonexistent_user_not_found(self):
        payload = {'login': generate_random_string(10), 'password': generate_random_string(10)}
        response = requests.post(f'{BASE_URL}/courier/login', data=payload)
        assert response.status_code == 404
        assert response.json()['message'] == 'Учетная запись не найдена'
