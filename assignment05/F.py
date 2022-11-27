content = open('num.csv', 'r').read()
content = content.split(',')
numbers = [int(num) for num in content]

tt = input()
if '+' in tt:
    print(numbers[1] + numbers[0])
elif '-' in tt:
    print(numbers[0] - numbers[1])
else:
    print('fake problem')