import pandas as pd
import numpy as npy

n = int(input())

tab = pd.DataFrame(columns=['id', 'to', 'bo', 'bo_'])
for i in range(n):
    l = input().split(' ')
    l.append(pd.NA)
    tab.loc[i] = l
    tab.loc[i]['bo_'] = int(l[2]) / int(l[1]) * 100

# print(tab)
tab[['to']] = tab[['to']].astype(npy.int16)
tab[['bo']] = tab[['bo']].astype(npy.int16)
tmp = npy.array(tab['to'])
avg1 = tmp.sum() / len(tmp)
tmp = npy.array(tab['bo'])
avg2 = tmp.sum() / len(tmp)
tab = tab[tab['to'] > avg1]
tab = tab[tab['bo'] >= avg2]

if len(tab) == 0:
    print('None')
else:
    for index, row in tab.iterrows():
        print('{:s} {:.2f}'.format(row['id'], row['bo_']))

