# -*- coding: utf-8 -*-
protein = float(input('Введите количество белков: '))
fats = float(input('Введите число жиров: '))
sugars = float(input('Введите число углеводов '))
kkal = (protein*4) + (fats*9) + (sugars*4)
print(f'{kkal}')
