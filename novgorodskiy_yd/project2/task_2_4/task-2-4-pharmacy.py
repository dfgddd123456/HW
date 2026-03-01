# -*- coding: utf-8 -*-
capsules = int(input('Число капсул'))
capacity = int(input('Вместимость упаковки'))
packages = capsules//capacity
other = capsules%capacity
print(f'Число полных упаковок{packages}')
print(f'Число оставшихся капсул{other}')