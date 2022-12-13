import pandas as pd

l = input().split(' ')
a, b = int(l[0]), int(l[1])

res = {}
for i in range(a):
    l = input().split(' ')
    res.update({l[0]: l[1:]})

res = pd.DataFrame(res)
print(res)