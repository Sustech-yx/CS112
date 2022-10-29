line = input()
line = line.upper()
cnt = 0
for ch in line:
    if ch == 'G' or ch == 'C':
        cnt += 1
# print(cnt / len(line))
if 0.4 >= cnt / len(line):
    print('GC too low')
elif 0.4 < cnt / len(line) < 0.6:
    print('OK')
else:
    print('GC too high')