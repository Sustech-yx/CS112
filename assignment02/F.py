words = input().split(' ')

# a = 'cba'
# a = ''.join(sorted(a))
# print(a)

ss = set()
for word in words:
    tmp = ''.join(sorted(word))
    ss.add(tmp)
print(len(ss))
# FILE MODIFY