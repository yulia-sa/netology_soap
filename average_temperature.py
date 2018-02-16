'''
Задача №1
Дано: семь значений температур по Фаренгейту в файле temps.txt.
Необходимо вывести среднюю за неделю арифметическую температуру по Цельсию.
'''

import os
import osa
import re


currencies = "currencies"
current_dir = os.path.dirname(os.path.abspath(__file__))
files_dir = os.path.join(current_dir, currencies)
path_to_file_temps = os.path.join(files_dir, "temps.txt")


client = osa.Client('http://www.webservicex.net/ConvertTemperature.asmx?WSDL')


def convert_temperature_in_celsius(Temperature, FromUnit='degreeFahrenheit', ToUnit='degreeCelsius'):
    return client.service.ConvertTemp(Temperature, FromUnit, ToUnit)

def get_average_temperature_in_celsius(path_to_file):
    with open(path_to_file_temps, encoding="utf-8") as f:
        text = f.read()
        temperature_list_celsius = []
        temperature_list_fahrenheit = re.findall('\d+', text)
        for temperature_in_fahrenheit in temperature_list_fahrenheit:
            temperature_in_celsius = convert_temperature_in_celsius(Temperature=temperature_in_fahrenheit, 
                                                                    FromUnit='degreeFahrenheit', 
                                                                    ToUnit='degreeCelsius')
            temperature_list_celsius.append(temperature_in_celsius)

        average_temperature_in_celsius = sum(temperature_list_celsius)/len(temperature_list_celsius)
        return print("Average temperature in Celsius: " + str(round(average_temperature_in_celsius, 1)))

 
get_average_temperature_in_celsius(path_to_file_temps)
