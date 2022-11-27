import numpy as npy
# FILE MODIFY
A = npy.array([[[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]], [[12, 13, 14, 15], [16, 17, 18, 19], [20, 21, 22, 23]]])
i = list(map(int, input().strip().split()))
if len(i) == 1:
    A += i[0]
elif len(i) == 2:
    A[0, :, :] += i[0]
    A[1, :, :] += i[1]
elif len(i) == 3:
    A[:, 0, :] += i[0]
    A[:, 1, :] += i[1]
    A[:, 2, :] += i[2]
elif len(i) == 4:
    A[:, :, 0] += i[0]
    A[:, :, 1] += i[1]
    A[:, :, 2] += i[2]
    A[:, :, 3] += i[3]
else:
    print('ERROR')
    exit(0)
print(A.tolist())