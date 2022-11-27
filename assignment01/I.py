s = input()
tot = len(s)

cnt = 0
for ch in s:
    if ch == 'C' or ch == 'G':
        cnt += 1
print('{:.2f}%'.format(float(cnt / tot) * 100))
# FILE MODIFY