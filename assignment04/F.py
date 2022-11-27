n = int(input())
f0 = int(input())
f1 = int(input())
# FILE MODIFY
a, b = f0, f1
c = f0 if n == 0 else f1
for i in range(2, n+1):
    c = a + b
    a, b = b, c
print(c)