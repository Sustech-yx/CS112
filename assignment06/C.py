import datetime as dt

mon_str = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sept', 10: 'Oct',
           11: 'Nov', 12: 'Dec'}
wek_str = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thur', 4: 'Fri', 5: 'Sat', 6: 'Sun'}


def _0(y, m, d, h, mi, s) -> str:
    return '%d-%02d-%02d' % (y, m, d)


def _1(y, m, d, h, mi, s) -> str:
    return '%02d:%02d:%02d' % (h, mi, s)


def _2(y, m, d, h, mi, s) -> str:
    d = dt.date(year=y, month=m, day=d)
    return '%s%%%s' % (wek_str[d.weekday()], mon_str[m])


i = list(map(int, input().split(' ')))
y = i[0]
m = i[1]
d = i[2]
h = i[3]
mi = i[4]
s = i[5]
func = {0: _0, 1: _1, 2: _2}
ty = input()
print(func[int(ty)](y, m, d, h, mi, s))