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
import math


files = "files"
current_dir = os.path.dirname(os.path.abspath(__file__))
path_to_file_currencies = os.path.join(current_dir, files, "currencies.txt")


client = osa.Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')


def convert_currency_to_rub(licenseKey, fromCurrency, toCurrency, amount, rounding, date, type):
    return client.service.ConvertToNum(licenseKey, fromCurrency, toCurrency, amount, rounding, date, type)


def get_full_travel_cost_in_rub(path_to_file_currencies):
    with open(path_to_file_currencies, encoding="utf-8") as f:
        text = f.read()
        costs_in_rub = []
        costs_in_currency = re.findall('\d+\s\D{3}', text)

        for x in costs_in_currency:
            fromCurrency = re.findall('[A-Za-z]{3}', x)
            amount = re.findall('\d+', x)

            x_to_rub = convert_currency_to_rub(licenseKey='', fromCurrency=fromCurrency, toCurrency='RUB', 
                                                amount=amount, rounding='false', date='', type='')
            costs_in_rub.append(math.ceil(x_to_rub))

        full_travel_cost_in_rub = sum(costs_in_rub)


    return print("Full travel cost: " + str(full_travel_cost_in_rub) + " RUB")


get_full_travel_cost_in_rub(path_to_file_currencies)

  
