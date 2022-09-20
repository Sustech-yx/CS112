ff = float(input())

cc = (ff-32)*5/9
res = '{:.4g}'.format(cc)
if len(res) < 4:
    res += '.'
while len(res) - 1 < 4:
    res += '0'
print(res)