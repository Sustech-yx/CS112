names = input().split(',')
names = list(set(names))
names = sorted(names)
# print(names)
print(len(names))
for name in names:
    print(name, end='\n')