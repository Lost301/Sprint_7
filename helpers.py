import random
import string

import allure
import requests

BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1'


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


@allure.step('Регистрируем нового курьера')
def register_new_courier():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    payload = {'login': login, 'password': password, 'firstName': first_name}
    response = requests.post(f'{BASE_URL}/courier', data=payload)
    if response.status_code == 201:
        return [login, password, first_name]
    return []


@allure.step('Логиним курьера {login} и получаем его id')
def login_courier(login, password):
    payload = {'login': login, 'password': password}
    response = requests.post(f'{BASE_URL}/courier/login', data=payload)
    if response.status_code == 200:
        return response.json().get('id')
    return None


@allure.step('Удаляем курьера с id {courier_id}')
def delete_courier(courier_id):
    return requests.delete(f'{BASE_URL}/courier/{courier_id}')


def order_payload(colors=None):
    payload = {
        'firstName': generate_random_string(6),
        'lastName': generate_random_string(6),
        'address': 'Москва, Тверская 1',
        'metroStation': 4,
        'phone': '+79999999999',
        'rentTime': 5,
        'deliveryDate': '2026-01-01',
        'comment': generate_random_string(10),
    }
    if colors is not None:
        payload['color'] = colors
    return payload


@allure.step('Создаём заказ с цветами {colors}')
def create_order(colors=None):
    response = requests.post(f'{BASE_URL}/orders', json=order_payload(colors))
    return response


@allure.step('Отменяем заказ с треком {track}')
def cancel_order(track):
    return requests.put(f'{BASE_URL}/orders/cancel', params={'track': track})
