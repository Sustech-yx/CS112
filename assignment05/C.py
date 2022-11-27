def genPrim(n: int) -> list:
    def check(t: int) -> bool:
        if t <= 1:
            return False
        if t in [2, 3, 5]:
            return True
        for j in range(2, int(pow(t, 0.5)) + 1):
            # print(j)
            if t % j == 0:
                return False
        return True

    res = []
    for i in range(n):
        if check(i):
            res.append(i)
    return res


prim_list = genPrim(1009)
# print(prim_list)
fileName = input()
# fileName = './TestFiles/C'
# FILE MODIFY
content = open(fileName, 'r').read()
numbers = content.split(' ')
# print(numbers)
numbers = [int(num) for num in numbers]
# numbers = [num for num in range(3, 1000000)]

res = []
for num in numbers:
    # if num == 1:
    fac = {}
    tmp = []
    for p in prim_list:
        if num == 1:
            break
        while num % p == 0:
            if p not in fac:
                fac[p] = 1
            else:
                fac[p] += 1
            num = num // p
    for k, v in fac.items():
        tmp.append(f'{k}:{v}')
        # print(, end=' ')
        # prime factors and their powers
    res.append(' '.join(tmp))
print('\n'.join(res))

