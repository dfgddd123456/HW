import pandas as pd
df = pd.read_csv('wild_boars.csv')
for col in df.columns[2:]:
        cont = df[col].median()
        with open('median_values.txt', 'a+', encoding='utf-8') as med:
            med.write(col)
            med.write(': ')
            med.write(f'{cont:.2f}\n')