import numpy as npy

n = int(input())
mat = npy.zeros((n, 4), dtype=npy.float64)

for i in range(n):
    l = input().split(' ')
    mat[i][0] = int(l[0])
    mat[i][1] = int(l[1])
    mat[i][2] = int(l[2])
    mat[i][3] = mat[i][2] / mat[i][1]

avg = npy.sum(mat, axis=0) / n
for i in range(n):
    if mat[i][1] > avg[1] and mat[i][2] >= avg[2]:
        print('{:s} {:.2f}'.format(str(int(mat[i][0])), mat[i][3] * 100))

# 3
# 1 100 90
# 2 50 45
# 3 30 20