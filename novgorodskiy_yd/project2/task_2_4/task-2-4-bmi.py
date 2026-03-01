# -*- coding: utf-8 -*-
weight = float(input('Введите ваш вес'))
height = float(input('Введите ваш рост'))
imt = weight / height**2
print(f'Рост\t{height}\nВес\t{weight}\nИМТ\t{imt}')
