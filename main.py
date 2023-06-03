a = input('Введите матемотическое выражение:\n')
b = a.split(' ')
if b[1] == '+':
    print(a, '=', int(b[0]) + int(b[2]))