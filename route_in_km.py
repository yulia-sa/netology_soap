'''
Задача №3
Дано: длина пути в милях, название пути (файл travel.txt) в формате:

<название пути>: <длина в пути> <мера расстояния>
Пример:
MOSCOW-LONDON: 1,553.86 mi
Необходимо посчитать суммарное расстояние пути в километрах с точностью до сотых.
'''

import os
import osa
import re


files = "files"
current_dir = os.path.dirname(os.path.abspath(__file__))
path_to_file_travel = os.path.join(current_dir, files, "travel.txt")


client = osa.Client('http://www.webservicex.net/length.asmx?WSDL')


def convert_miles_to_km(length_value, from_length_unit, to_length_unit):
    return client.service.ChangeLengthUnit(length_value, from_length_unit, to_length_unit)


def get_full_route_in_km(path_to_file_travel):
    with open(path_to_file_travel, encoding="utf-8") as f:
        text = f.read()
        parts_of_route_in_km = []
        raw_parts_of_route_in_miles = re.findall('[0-9]{1,}\,{0,1}[0-9]{0,}\.{0,1}[0-9]{0,}', text)

        for raw_part in raw_parts_of_route_in_miles:
            part = raw_part.replace(',', '')
            length_value = float(part)
            part_in_km = convert_miles_to_km(length_value=length_value, from_length_unit='Miles',
                                             to_length_unit='Kilometers')
            parts_of_route_in_km.append(part_in_km)

        full_route_in_km = round(sum(parts_of_route_in_km), 2)

    return print("Full route: " + str(full_route_in_km) + " km")


get_full_route_in_km(path_to_file_travel)
