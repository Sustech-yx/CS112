import numpy as npy


def check(mat):
    return npy.all(mat == mat.T)
# FILE MODIFY

n = int(input())
arr1 = npy.zeros(shape=(n, n), dtype=npy.int64)
for i in range(n):
    l = list(map(int, input().strip().split()))
    arr1[i] += l
arr2 = npy.zeros(shape=(n, n), dtype=npy.int64)
for i in range(n):
    l = list(map(int, input().strip().split()))
    arr2[i] += l
a, b = check(arr1), check(arr2)
if a and b:
    print(arr1 + arr2)
elif a or b:
    print(npy.matmul(arr1, arr2))
else:
    print('not favorable')