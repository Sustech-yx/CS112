# from queue import SimpleQueue

ll = input()
s = []
n = len(ll)
yes, no = 'True', 'False'
for i in range(n):
    if ll[i] in ['(', ')']:
        if len(s) == 0 or ll[i] == '(':
            s.append(ll[i])
        elif ll[i] == ')' and s.pop() == '(':
            pass
        else:
            print(no)
            exit(0)
print(yes if len(s) == 0 else no)
