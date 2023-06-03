a = input('Введите матемотическое выражение:\n')
b = a.split(' ')
if b[1] == '+':
    print(a, '=', int(b[0]) + int(b[2]))
elif b[1] == '-':
    print(a, '=', int(b[0]) - int(b[2]))
elif b[1] == '*':
    print(a, '=', int(b[0]) * int(b[2]))
elif b[1] == '/':
    try:
        print(a, '=', int(b[0]) / int(b[2]))
    except ZeroDivisionError:
        print('На ноль делить нельзя')    