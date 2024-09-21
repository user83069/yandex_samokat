# Импорт библиотеки requests для выполнения HTTP-запросов
import sender_stand_request

# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data

def get_new_track(order_response):
    return order_response.json().get("track")

data.params_get["t"] = get_new_track(sender_stand_request.order_response)

# Автотест
def positive_assert():
    track_response = sender_stand_request.get_order(data.params_get)
    assert track_response.status_code == 200

def test_order():
    positive_assert()
