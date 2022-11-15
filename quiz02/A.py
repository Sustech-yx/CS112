n = int(input())

check = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
checker = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
yes = 'YES'
no = 'NO'
for _ in range(n):
    ll = input()
    tt = 0
    for i in range(17):
        tt += check[i] * int(ll[i])
    if checker[tt % 11] == ll[-1]:
        print(yes)
    else:
        print(no)