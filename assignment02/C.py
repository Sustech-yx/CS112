l1 = input().split(' ')
il1 = []
for i in l1:
    il1.append(int(i))
l2 = input().split(' ')
il2 = []
for i in l2:
    il2.append(int(i))

tmp = list(zip(il1, il2))
tmp = sorted(tmp, key=lambda x: x[0], reverse=False)

for (i, j) in tmp:
    print(j, end=' ')