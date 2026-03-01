# -*- coding: utf-8 -*-
a = input("Введите название среды:")
b = input("Введите концентрацию агара (в процентах):")
с = input("Введите температуру стерилизации:")
d = a.upper()
with open(f'recipe.txt', "w", encoding="utf-8") as file:
    file.write(f"{d}\n")
    file.write(f"Концентрация агара: {b} \nТемпература стерилизации: {с}")
print("Файл 'recipe.txt' успешно сформирован!")