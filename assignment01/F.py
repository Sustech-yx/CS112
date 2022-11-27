s = input()
l = s.split(' ')
res = []
for ss in l:
    if int(ss) != 0:
        res.append(int(ss))
while len(res) < 5:
    # print('foo')
    res.append(0)
for i in [0, 1, 2, 3]:
    print(res[i], end=' ')
print(res[4])
# FILE MODIFY