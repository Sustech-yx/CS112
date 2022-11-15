import calendar

n = int(input())

yes = 'YES'
no = 'NO'

for _ in range(n):
    if calendar.isleap(int(input())):
        print(yes)
    else:
        print(no)