'''
Задача №2
Вы собираетесь отправиться в путешествие и начинаете разрабатывать маршрут и выписывать цены на перелеты.
Даны цены на билеты в местных валютах (файл currencies.txt). Формат данных в файле:
<откуда куда>: <стоимость билета> <код валюты>
Пример:
MOSCOW-LONDON: 120 EUR
Посчитайте, сколько вы потратите на путешествие денег в рублях (без копеек, округлить в большую сторону).
'''

import os
import osa
import re


currencies = "currencies"
current_dir = os.path.dirname(os.path.abspath(__file__))
files_dir = os.path.join(current_dir, currencies)
path_to_file_currencies = os.path.join(files_dir, "currencies.txt")

