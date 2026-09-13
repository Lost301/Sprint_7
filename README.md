# Sprint_7

Финальный проект 7 спринта: автотесты API учебного сервиса «Яндекс.Самокат».

Документация API: https://qa-scooter.praktikum-services.ru/docs/

## Что покрыто тестами

Основное задание:

- Создание курьера — `tests/test_create_courier.py`
- Логин курьера — `tests/test_login_courier.py`
- Создание заказа — `tests/test_create_order.py`
- Получение списка заказов — `tests/test_get_orders_list.py`

Дополнительное задание:

- Удаление курьера — `tests/test_delete_courier.py`
- Принятие заказа — `tests/test_accept_order.py`
- Получение заказа по номеру — `tests/test_get_order_by_track.py`

## Структура проекта

- `tests/` — тесты: один класс на ручку;
- `helpers.py` — генерация тестовых данных и шаги Allure;
- `conftest.py` — фикстуры: создание курьера/заказа перед тестом и удаление после;
- `allure_results/` — сырые результаты прогона (JSON);
- `allure_report/` — сгенерированный Allure-отчёт.

## Как запустить

```bash
pip install -r requirements.txt
pytest --alluredir=allure_results
allure generate allure_results -o allure_report --clean
```

Отчёт откроется в браузере командой `allure serve allure_results`.
