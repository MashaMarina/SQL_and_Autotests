import configuration
import requests
import data

# Создание заказа
def get_track():
    response = requests.post(configuration.URL + configuration.CREATE_ORDER_PATH, json=data.order_body)
    if response.status_code == 201:        # если код ответа 201 то вернуть track
        return response.json()['track']

# Получение инфо о заказе
def get_order(track):
    return requests.get(configuration.URL + configuration.GET_ORDER_PATH + str(track))

def post_new_order(body):
    return requests.post(configuration.URL + configuration.CREATE_ORDER_PATH, json=body)
response = post_new_order(data.order_body)

print(response.status_code)


track = get_track()
print(track)
print(get_order(track))