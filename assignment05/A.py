import re

fileName = input()
# fileName = './TestFiles/A'
# FILE MODIFY
content = open(fileName, 'r').read()

# print(content)

content = content.replace('-', '')
res = re.findall(r'[a-zA-Z]*', content)
cnt = 0
for tt in res:
    if tt != '':
        cnt += 1
print(cnt)

# print(content)