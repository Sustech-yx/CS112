line = input()

for mark in ['*', '+', '-']:
    if len(line.split(mark)) != 1:
        cal = line.split(mark)
        var = cal[0] = int(cal[0])
        cal[1] = int(cal[1])
        if mark == '*':
            print(cal[0] * cal[1])
        elif mark == '+':
            print(cal[0] + cal[1])
        elif mark == '-':
            print(cal[0] - cal[1])
        else:
            print('fake problem')
            # FILE MODIFY