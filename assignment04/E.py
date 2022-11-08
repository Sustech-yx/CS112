import numpy as npy


magic_square = ([[17, 24, 1, 8, 15],
                 [23, 5, 7, 14, 16],
                 [4, 6, 13, 20, 22],
                 [10, 12, 19, 21, 3],
                 [11, 18, 25, 2, 9]])

arr = npy.array(magic_square)
n = int(input())
arr -= n
arr = npy.abs(arr)
ma = npy.unravel_index(npy.argmax(arr), arr.shape)
mi = npy.unravel_index(npy.argmin(arr), arr.shape)
print(abs(magic_square[ma[0]][ma[1]] - n) - abs(magic_square[mi[0]][mi[1]] - n))
