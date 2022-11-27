import json
import pandas as pd

n = int(input())
# FILE MODIFY
header = None
res = []
for _ in range(n):
    line = input()
    obj = json.loads(line)
    if header is None:
        header = obj.keys()
    res.append(obj)

print(', '.join(header))
for obj in res:
    tmp = []
    for k in header:
        # print(obj[k])
        tmp.append(str(obj[k]))
    print(', '.join(tmp))