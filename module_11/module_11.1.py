from io import BytesIO
from PIL import Image
import requests
import pandas
import numpy
import matplotlib.pyplot as plt
import random

# from requests import *
# Создаём переменную, в которую сохраним код состояния запрашиваемой страницы.
'''
response = requests.get('https://everythink.ru') 
print(response) # проверяем на ошибки
print(response.content) # получаем содержание страницы в бафтовом виде
print(response.text) # декодировка страницы из байтового вида в строковый
# это получение json текста, который можно использовать как словарь
print(response.headers) # получение информации из заголовка, инф о странице

GET - метод используется для обычного запроса к серверу и получения информации по URL.
POST - Метод запроса POST запрашивает веб-сервис для приёма данных, например для хранения информации.
PUT	- Метод PUT просит, чтобы вложенный в него объект был сохранён под определённым URI. Если URI ссылается на уже существующий ресурс, он модифицируется, а если URI указывает на несуществующий ресурс, сервер может создать новый ресурс с этим URI.
DELETE - Метод DELETE удаляет объект с сервера.
HEAD - Метод HEAD запрашивает ответ, идентичный запросу GET, но без тела ответа.
PATCH - Метод используется для модификации информации на сервере.'''

# поиск изображения на сайте
params ={'q': 'Pony', 'order': 'popular', 'min_width': '1000', 'min_height': '800'}
response = requests.get('https://yandex.ru/images/', params=params)
print(response)
print(response.url) # вывод ссылки с ответом

# from requests import *
# получим картинку с окрестностями на яндекс карте

# приводим параметры в читабельный вид
# 11 координаты центра карты
# spn определяет область показа (протяжённость карты в градусах по долготе и широте)
# l определяет тип карты

params = {"ll": "37.935806,54.759223",
          "spn": "0.01646,0.0062",
          "l": "map"}

try:
    response = get("https://static-maps.yandex.ru/1.x/", params=params)
    print(response) # проверяем ответ программы на ошибки
except ConnectionError:
    print("Проверьте подключение к сети.")
else:
    with open("map.png", "wb") as file:
        file.write(response.content)


# from requests import *
# from pillow import *
# Скачаю с сайта картинку и изменю ее

response = requests.get('https://www.parazitakusok.ru/images/item/5208/MOD.jpg')
img_data = response.content
image = Image.open(BytesIO(img_data))
image.show() # показать картинку
image_path = f'c:/PythonProjects/My_python/module_11/my_pony.png'
image.save(image_path) # сохранение
image = image.crop((10, 10, 10, 10)) # обрезка
image.save(image_path)
image = image.rotate(90) # развернуть
image.save(image_path)


# import matplotlib.pyplot as plt
# визуализировать данные с помощью библиотеки любым удобным для вас инструментом из библиотеки.

# график
x = [i for i in range(1,11)] #Для начала создадим две переменные — x и y ОДИНАКОВОЙ ДЛИНЫ
y = [1, 5, 46, 32, 65, 45, 21, 12, 10, 36]
plt.plot(x, y, color='green', marker='o', markersize=7) #Теперь построим график, который соединит эти точки:
plt.xlabel('Ось х') #Подпись для оси х
plt.ylabel('Ось y') #Подпись для оси y
plt.title('Случайный график') #Название
plt.show()

# столбчатая диаграмма
x = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май']
y = [2, 4, 3, 1, 7]

plt.bar(x, y, label='Величина прибыли') #Параметр label позволяет задать название величины для легенды
plt.xlabel('Месяц года')
plt.ylabel('Прибыль, в млн руб.')
plt.title('Пример столбчатой диаграммы')
plt.legend()
plt.show()

# объединяем
x = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май']
y = [2, 4, 3, 1, 7]

plt.bar(x, y, label='Величина прибыли') #Параметр label позволяет задать название величины для легенды
plt.plot(x, y, color='green', marker='o', markersize=7)

plt.xlabel('Месяц года')
plt.ylabel('Прибыль, в млн руб.')
plt.title('Комбинирование графиков')
plt.legend()
plt.show()

# круговая диаграмма
vals = [24, 17, 53, 21, 35]
labels = ["Ford", "Toyota", "BMW", "Audi", "Jaguar"]
plt.pie(vals, labels=labels, autopct='%1.1f%%')
plt.title("Распределение марок автомобилей на дороге")
plt.show()
