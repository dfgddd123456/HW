import pandas as pd
df = pd.read_csv('wild_boars.csv')
for col in df.columns[1:]:
        cont = df[col].mode()
        with open('mode_values.txt', 'a+', encoding='utf-8') as mod:
            mod.write(f'{cont}\n')