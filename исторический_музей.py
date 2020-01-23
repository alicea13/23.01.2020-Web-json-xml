import requests

geocoder_request = "https://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0,%20%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%B0%D1%8F,%20%D0%BF%D0%BB%D0%BE%D1%89%D0%B0%D0%B4%D1%8C,%201&format=json"

# Выполняем запрос.
response = requests.get(geocoder_request)
if response:
    # Преобразуем ответ в json-объект
    json_response = response.json()

    # Получаем первый топоним из ответа геокодера.
    # Согласно описанию ответа, он находится по следующему пути:
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    # Полный адрес топонима:
    toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
    # Координаты центра топонима:
    toponym_coodrinates = toponym["Point"]["pos"]
    # Печатаем извлечённые из ответа поля:
    print(toponym_address, "имеет координаты:", toponym_coodrinates)
else:
    print("Ошибка выполнения запроса:")
    print(geocoder_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
