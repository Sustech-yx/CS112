n = int(input())
mat1 = []
for i in range(n):
    tmp = input().split(' ')
    for j in range(len(tmp)):
        tmp[j] = int(tmp[j])
    mat1.append(tmp)

tp = input()
mat2 = []
for i in range(n):
    tmp = input().split(' ')
    for j in range(len(tmp)):
        tmp[j] = int(tmp[j])
    mat2.append(tmp)
# FILE MODIFY
try:
    res = []
    if len(mat1[0]) != len(mat2[0]):
        print('error')
        exit(0)
    if tp == 'add':
        for i in range(n):
            tmp = []
            for j in range(len(mat1[0])):
                tmp.append(mat1[i][j] + mat2[i][j])
            res.append(tmp)
        print(res)
    elif tp == 'multiply':
        for i in range(n):
            tmp = []
            for j in range(len(mat1[0])):
                tmp.append(mat1[i][j] * mat2[i][j])
            res.append(tmp)
        print(res)
    elif tp == 'substract':
        for i in range(n):
            tmp = []
            for j in range(len(mat1[0])):
                tmp.append(mat1[i][j] - mat2[i][j])
            res.append(tmp)
        print(res)
    else:
        print('fake problem')
except IndexError:
    print('error')