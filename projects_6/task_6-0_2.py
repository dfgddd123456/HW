import pandas as pd
df = pd.read_csv('wild_boars.csv')
for col in df.columns[2:]:
        cont = df[col].mean()
        with open('mean_values.txt', 'a+', encoding='utf-8') as means:
            means.write(col)
            means.write(': ')
            means.write(f'{cont:.2f}\n')