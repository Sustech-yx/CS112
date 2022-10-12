A = 'MDDDIAALVVDNGSGMCKAGF'
B = input()

a_m = {}
b_m = {}

for i in range(len(A)):
    a_m[A[i]] = True

for i in range(len(B)):
    b_m[B[i]] = True

a_k = a_m.keys()
b_k = b_m.keys()

print('{:.4f}'.format(len(a_k & b_k) / len(a_k | b_k)))
