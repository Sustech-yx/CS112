mm = {}
ll = []

for i in range(6):
    t = input()
    ll.append(t)
    mm.setdefault(t, 0)
# The keys should be treated as strings when sorting.
for i in ll:
    mm[i] += 1
keys = list(mm.keys())
keys = sorted(keys)
for key in keys:
        # print(key + ': ' + str(mm[key]))
    print(key + ': ' + str(mm[key]))
