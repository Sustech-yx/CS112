import pandas as pd

name = input()
df = pd.read_csv(name, sep='\t')
# print(df)
df.insert(loc=4, column='padjust', value=10*df['p_value'])
df = df[df['p_value'] < 0.05]
# print(df)
df = df[df['label']]
print(df)

