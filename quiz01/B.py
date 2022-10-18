# Store1 2000
# Store2 1900
# Store3 2100

a, b, c = input().split(' '), input().split(' '), input().split(' ')
ll = [a, b, c]
ll[0][1] = int(ll[0][1])
ll[1][1] = int(ll[1][1])
ll[2][1] = int(ll[2][1])

ll = sorted(ll, key=lambda x:x[1])
print(ll[0][0])