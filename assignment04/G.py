yes = 'They can create a triangle'
no_ = 'They can NOT create a triangle'

a, b, c = map(int, input().strip().split())
if a + c > c and a + c > b and b + c > a:
    print(yes)
else:
    print(no_)