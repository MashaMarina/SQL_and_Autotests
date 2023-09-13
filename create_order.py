# Мария Марина, 8-я когорта — Финальный проект. Инженер по тестированию плюс

import requests
import configuration
import data

import sender_stand_request as ssr
track = ssr.get_track()

def get_order_positive(track):           # эта функция меняет значения в параметре track
    # Подготовка данных
    current_order_body = data.order_body.copy()  # копируем словарь для  передачи body
    current_order_body['track'] = track  # помещаем track в body
    response = ssr.get_order(track)
    assert response.status_code == 200

    assert response.json()['track'] == track


# Тест 1. Успешное получение заказа по номеру
def test_create_order_success_response():
    order_response = ssr.get_order(track)
    assert order_response.status_code == 200

