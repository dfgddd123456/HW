import pandas as pd
df = pd.read_csv('wild_boars.csv')
for col in df.columns[2:]:
        with open('percentile_values.txt', 'a+', encoding='utf-8') as perc:
            perc.write(col)
            perc.write(':\n')
            perc.write(f"Percentile 25 (Q1):\t{df[col].quantile(0.25):.1f}\n")
            perc.write(f"Median 50 (Q2):\t{df[col].quantile(0.50):.1f}\n")
            perc.write(f"Percentile 75 (Q3):\t{df[col].quantile(0.75):.1f}\n")
            perc.write(f"Percentile 90:\t{df[col].quantile(0.90):.1f}\n")
            perc.write(f"Percentile 95:\t{df[col].quantile(0.95):.1f}\n")
            perc.write(f"Max:\t{df[col].quantile(1.00):.1f}\n\n")