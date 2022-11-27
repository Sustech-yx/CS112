n = int(input())

cnt = 1
for i in range(n // 2 + 1):
    print(' ' * ((n - cnt) // 2), end='')
    print('*' * cnt, end='')
    print(' ' * ((n - cnt) // 2), end='' if cnt == n else '\n')
    cnt = cnt + 2
    # FILE MODIFY