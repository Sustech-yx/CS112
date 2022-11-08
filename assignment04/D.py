l = list(map(int, input().strip().split()))


def check(i: int) -> bool:
    if i <= 1:
        return False
    if i in [2, 3, 5]:
        return True
    for j in range(2, int(pow(i, 0.5)) + 1):
        # print(j)
        if i % j == 0:
            return False
    return True


for num in l:
    print(check(num))