from computing import *

if __name__ == '__main__':
    a = input('Введите матемотическое выражение:\n')
    input_value = a.split(' ')
    result = 0
    
    for i in range(0, len(input_value) -2, 2):
        if i == 0:
            result = int(input_value[0])
        result = compute(result, int(input_value[i + 2]), input_value[i+1])
    print(result)