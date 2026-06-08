import pandas as pd
df = pd.read_csv('wild_boars.csv')

std_tusk = df.groupby('gender')['tusk_length_cm'].std()
mean_tusk = df.groupby('gender')['tusk_length_cm'].mean()

with open('tusk_length.txt' , 'w', encoding='utf-8') as tusks:
    tusks.write(f'Coefficient of task length variation: {(std_tusk / mean_tusk * 100)}')