import allure
import pytest

from helpers import cancel_order, create_order, delete_courier, login_courier, register_new_courier


@pytest.fixture
def courier_credentials():
    with allure.step('Создаём тестового курьера'):
        credentials = register_new_courier()
    yield credentials
    with allure.step('Удаляем тестового курьера'):
        courier_id = login_courier(credentials[0], credentials[1])
        if courier_id is not None:
            delete_courier(courier_id)


@pytest.fixture
def courier_id(courier_credentials):
    return login_courier(courier_credentials[0], courier_credentials[1])


@pytest.fixture
def order_track():
    with allure.step('Создаём тестовый заказ'):
        track = create_order().json().get('track')
    yield track
    with allure.step('Отменяем тестовый заказ'):
        cancel_order(track)


@pytest.fixture
def created_tracks():
    tracks = []
    yield tracks
    with allure.step('Отменяем созданные в тесте заказы'):
        for track in tracks:
            cancel_order(track)
