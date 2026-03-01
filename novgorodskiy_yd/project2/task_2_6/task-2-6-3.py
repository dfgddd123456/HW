# -*- coding: utf-8 -*-
donor = input('Группа крови донора: ').strip().upper()
recipient = input('Группа крови ацептора: ').strip().upper()
if donor == recipient or donor == 'I':
    print('Переливать можно')
else:
    print('Переливать нельзя') 
