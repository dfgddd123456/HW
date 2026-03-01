# -*- coding: utf-8 -*-
dna = input('Введите последовательность нуклеотидов: ')
count = len(dna)
dna_big = dna.upper()
count_A = dna_big.count('A')
A_perc = count_A/count * 100
count_T = dna_big.count('T')
T_perc = count_T/count * 100
count_G = dna_big.count('G')
G_perc = count_G/count * 100
count_C = dna_big.count('C')
C_perc = count_C/count * 100
print('Подсчёт нуклеотидов:')
print(f'A:{count_A} {A_perc:.2f}%')
print(f'T:{count_T} {T_perc:.2f}%')
print(f'G:{count_G} {G_perc:.2f}%')
print(f'C:{count_C} {C_perc:.2f}%')
print(f'Всего нуклеотидов: {count}')