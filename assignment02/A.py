names1 = input().split(' ')
scores1 = input().split(' ')
names2 = input().split(' ')
scores2 = input().split(' ')

m1 = {}
m2 = {}

for index, name in enumerate(names1):
    m1[name] = scores1[index]
for index, name in enumerate(names2):
    m2[name] = scores2[index]

res = []
for key in m1.keys():
    if m1[key] == m2[key]:
        res.append(key)
res = sorted(res)
for name in res:
    print(name, end='\n')