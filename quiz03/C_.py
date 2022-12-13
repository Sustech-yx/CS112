menu = {}

with open('1.csv', 'r') as f:
    f.readline()
    line = f.readline()[:-1]
    while line is not None and line != '':
        line = line.split(',')
        line[1] = (float(line[1]), 1)
        if line[0] not in menu:
            menu[line[0]] = line[1]
        else:
            if line[1][0] < menu[line[0]][0]:
                menu[line[0]] = line[1]
        line = f.readline()

with open('2.csv', 'r') as f:
    f.readline()
    line = f.readline()[:-1]
    while line is not None and line != '':
        line = line.split(',')
        line[1] = (float(line[1]), 2)
        if line[0] not in menu:
            menu[line[0]] = line[1]
        else:
            if line[1][0] < menu[line[0]][0]:
                menu[line[0]] = line[1]
        line = f.readline()

with open('3.csv', 'r') as f:
    f.readline()
    line = f.readline()[:-1]
    while line is not None and line != '':
        line = line.split(',')
        line[1] = (float(line[1]), 3)
        if line[0] not in menu:
            menu[line[0]] = line[1]
        else:
            if line[1][0] < menu[line[0]][0]:
                menu[line[0]] = line[1]
        line = f.readline()

name = input()
if name not in menu:
    print('None')
else:
    print(menu[name][1], menu[name][0])