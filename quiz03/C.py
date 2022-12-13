import pandas as pd

store1 = pd.read_csv('1.csv')
store2 = pd.read_csv('2.csv')
store3 = pd.read_csv('3.csv')

name = input()
cheapest = 10e5
cheapest_store = -1

if len(store1[store1['Name']==name]) > 0:
    store1 = store1.loc[store1['Name']==name, 'Price']
    # print(store1)
    if cheapest > store1.iloc[0]:
        cheapest = store1.iloc[0]
        # print(cheapest)
        cheapest_store = 1
else:
    pass

if len(store2[store2['Name']==name]) > 0:
    store2 = store2.loc[store2['Name']==name, 'Price']
    # print(cheapest)
    # print(store2['Price'][0])
    if cheapest > store2.iloc[0]:
        cheapest = store2.iloc[0]
        cheapest_store = 2
else:
    pass

if len(store3[store3['Name']==name]) > 0:
    store3 = store3.loc[store3['Name']==name, 'Price']
    # index = store3['id'][0]
    # print(index)
    # print(store1['Price'])
    if cheapest > store3.iloc[0]:
        cheapest = store3.iloc[0]
        cheapest_store = 3
else:
    pass

if cheapest_store == -1:
    print('None')
    exit(0)

print(str(cheapest_store), end=' ')
print(cheapest)