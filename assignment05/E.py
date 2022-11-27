# fileName = input()
fileName = './TestFiles/E'
res = []
cnt = 0
with open(fileName, 'r') as file:
    while 1:
        cnt += 1
        line = file.readline()
        if line is None or line == '':
            break
        if cnt % 2 == 0:
            # print('foo')
            res.append(line[2:20] + '\n')
        else:
            # print('bar')
            res.append(line)

print(''.join(res), end='')