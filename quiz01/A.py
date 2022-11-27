a = input()
b = int(input())
b = b % len(a)
l_ = list(a)

for i in range(b):
    t = l_[-1]
    l_ = l_[0:-1]
    l_.insert(0, t)
    # print(l_)

print(''.join(l_)) # FILE MODIFY
