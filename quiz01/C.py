line1 = input().split(' ')
line2 = input().split(' ')
coor = list(zip(line1, line2))

res = 0.0
for i in range(3):
    c1 = coor[i]
    c2 = coor[(i+1)%3]
    res += ((float(c1[0]) - float(c2[0])) ** 2 + (float(c1[1]) - float(c2[1])) ** 2)**0.5
    # print(res)
print(round(res)) # FILE MODIFY