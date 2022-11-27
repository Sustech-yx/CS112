import calendar

n = int(input())

yes = 'YES'
no = 'NO'
# FILE MODIFY
for _ in range(n):
    if calendar.isleap(int(input())):
        print(yes)
    else:
        print(no)