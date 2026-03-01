# -*- coding: utf-8 -*-
a = input("Введите имя оператора:")
b = input("Введите текущее значение датчика:")
with open('sensor_log.txt', "w", encoding="utf-8") as file:
    file.write(f"{a}:\t{b}")
print("Данные успешно сохранены в sensor_log.txt")

