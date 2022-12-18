import pandas as pd

n = int(input())
name = []
gender = []
Age = []
Address = []
gender_code = []

for _ in range(n):
    line = input().split(', ')
    name.append(line[0])
    gender.append(line[1])
    Age.append(int(line[2]))
    Address.append(line[3])
    gender_code.append(1 if line[1] == 'M' else 0)

res = pd.DataFrame({'Name': name, 'Gender': gender, 'Age': Age, 'Address': Address, 'GenderCode': gender_code})
print(res)
tmp = res[res['Age'] > 30]
if len(tmp) == 0:
    print('None')
else:
    print(tmp)

tmp = res[res['Name'].str.startswith('J')]
if len(tmp) == 0:
    print('None')
else:
    print(tmp)