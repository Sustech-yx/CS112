t = input()
if t[-1] == 'C' or t[-1] == 'c':
    t = int(t[:-1])
    res = round(t * 9 / 5) + 32
    print(str(res) + 'F')
elif t[-1] == 'f' or t[-1] == 'F':
    t = int(t[:-1])
    res = round((t - 32) * 5 / 9)
    print(str(res) + 'C')
else:
    print('Invalid input')