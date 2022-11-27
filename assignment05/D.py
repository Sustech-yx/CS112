import os

dictionary = dict()
filepath = input()
sp_name = input()

res = []
for root, dirs, files in os.walk(filepath, topdown=False):
    for name in files:
        if sp_name in name:
            res.append(name)

res = sorted(res)
print('\n'.join(res), end='')