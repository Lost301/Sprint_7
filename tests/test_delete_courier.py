import allure
import requests

from constants import BASE_URL
from helpers import delete_courier, login_courier, register_new_courier


@allure.epic('Courier')
class TestDeleteCourier:
    @allure.title('Курьера можно удалить, передав его id')
    @allure.description('Проверяем, что успешное удаление возвращает 200 и {"ok": true}')
    def test_delete_courier_valid_id_deleted(self):
        credentials = register_new_courier()
        courier_id = login_courier(credentials[0], credentials[1])
        response = delete_courier(courier_id)
        assert response.status_code == 200
        assert response.json() == {'ok': True}

    @allure.title('Запрос удаления без id возвращает ошибку')
    @allure.description('Проверяем, что DELETE /courier/ без id возвращает 404')
    def test_delete_courier_no_id_not_found(self):
        response = requests.delete(f'{BASE_URL}/courier/')
        assert response.status_code == 404

    @allure.title('Запрос удаления с несуществующим id возвращает ошибку')
    @allure.description('Проверяем, что удаление курьера с несуществующим id возвращает 404')
    def test_delete_courier_nonexistent_id_not_found(self):
        response = delete_courier(999999999)
        assert response.status_code == 404
        assert response.json()['message'] == 'Курьера с таким id нет.'
