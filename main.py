def compute(arg1: int, arg2: int, operation: str):
    result = 0
    if operation == '+':
        result = arg1 + arg2
    elif operation == '-':
        result = arg1 - arg2
    elif operation == '*':
        result = arg1 * arg2
    elif operation == '/':
        try:
            result = arg1 + arg2
        except ZeroDivisionError:
            print('На ноль делить нельзя')    
    return result

a = input('Введите матемотическое выражение:\n')
b = a.split(' ')
print(compute(int(b[0]), int(b[2]), b[1]))
    
        