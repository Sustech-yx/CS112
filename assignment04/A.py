# import numpy as npy
#
#
# def circle(n):
#     theta = npy.linspace(0, npy.pi, n, endpoint=False)
#     # x, y = npy.cos(theta), npy.sin(theta)
#     return npy.cos(theta), npy.sin(theta)
#
#
# def calDist(x0, y0, x1, y1):
#     # y = kx
#     # A = 0 - y1, B = x1, C = x1 * y1 - x1 * y1
#     A = -y1
#     B = x1
#     C = 0
#     return abs((A * x0) + (B * y0) + C) / ((A ** 2 + B ** 2) ** 0.5)
#
#
# if __name__ == '__main__':
#     n = int(input())
#     line = input().split(' ')
#     x0, y0 = int(line[0]), int(line[1])
#     # print(x0, y0)
#     res = []
#     x1, y1 = circle(n)
#     for i in range(n):
#         res.append('{:.2f}'.format(calDist(x0, y0, x1[i], y1[i])))
#         # print('{:.2f}'.format(calDist(x0, y0, x1[i], y1[i])), end=' ')
#     print(' '.join(res))
#
# # import numpy as npy
# #
# # if __name__ == '__main__':
# #     n = int(input())
# #     line = input().split(' ')
# #     theta = npy.linspace(0, npy.pi, n, endpoint=False)
# #     x0, y0 = int(line[0]), int(line[1])
# #     # print(x0, y0)
# #     x1, y1 = npy.cos(theta), npy.sin(theta)
# #     for i in range(n):
# #         A = -y1[i]
# #         B = x1[i]
# #         print('{:.2f}'.format(abs((A * x0) + (B * y0)) / ((A ** 2 + B ** 2) ** 0.5)), end=' ')


import numpy as npy


def main():
    n = int(input())
    line = input().split(' ')
    x0, y0 = int(line[0]), int(line[1])
    theta = npy.linspace(0, npy.pi, n, endpoint=False)
    # print(x0, y0)
    k = npy.tan(theta)

    res = npy.abs(k * x0 - y0) / npy.sqrt(npy.power(k, 2) + 1)
    print(' '.join(('%.2f' % i) for i in res))
    # res = abs(((k * x0 - y0) / (1 + k ** 2) ** 0.5))
    # print(' '.join(res.tolist()))


main()