# Мария Марина, 8-я когорта — Финальный проект. Инженер по тестированию плюс

import requests
import configuration
import data

import sender_stand_request as ssr
track = ssr.get_track()

def get_order(track):
    # Подготовка данных
    current_order_body = data.order_body.copy()  # копируем словарь для  передачи body
    current_order_body['track'] = track  # помещаем track в body
    return current_order_body
    response = ssr.get_order(track)

    # Функция для позитивной проверки
def positive_assert(track):
        # В переменную order_body сохраняется обновленное тело запроса
    current_order_body = ssr.get_order(track)
        # В переменную order_response сохраняется результат запроса на создание заказа:
    response = ssr.get_order(track)
    assert response.status_code == 200             # Проверка, что код ответа равен 200
    assert response.json()['track'] == track  # Проверка, что в ответе поле track совпадает с полем track в запросе

# Функция для негативной проверки
def negative_assert(track=None):
    current_order_body = data.order_body.copy()

    if track is not None:
            current_order_body['track'] = track
    print(current_order_body)

    response = ssr.get_order(track)

    assert response.status_code == 400             # Проверка, что код ответа равен 400
    assert response.json()["code"] == 400          # Проверка, что в теле ответа атрибут "code" равен 400
    assert response.json()["message"] == "Недостаточно данных для поиска" # Проверка текста в теле ответа в атрибуте "message"

# Тест 1. Успешное получение заказа по номеру
def test_create_order_success_response():
    positive_assert('track')

def test_create_order_negative_response():
   negative_assert('')
