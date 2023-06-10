from ast import operator
from operator import le
from computing import *

if __name__ == '__main__':
    a = input('Введите математическое выражение:\n')
    input_value = a.split(' ')
    result = 0
    operators = []
    num = []
    if len(a) == 0:
        print('Ошибка. Ввод не может быть пустым')
    else:
        # if (len(input_value) - 1) % 2 != 0:
        #     print('Ошибка. Выражение должно быть полным')
        # else:
        #     for j in range(len(input_value)-1):
        #         num += input_value[::2] 
        #         oper += input_value[1::2]
        #     if num.isdigit():
        #         for i in range(0, len(input_value) -2, 2):
        #             if i == 0:
        #                 result = int(input_value[0])
        #             result = compute(result, int(input_value[i + 2]), input_value[i+1])
        #             print(result)    
        #     else:
        #         print('Ошибка')
        for i in range(len(input_value)):
            if i % 2 == 0:
                if (input_value[i].isdigit()) :
                    num.append(int(input_value[i]))
                else:
                    print('Parameter must be a number!!!')
            else:
                if (input_value[i] in accepted_operators()):
                    operators.append(input_value[i])
                else:
                    print('Unavailable operator')
        operator_index = 0
        for i in range(len(num) -1 ):
            if i == 0:
                result = num[0]
            result = compute(result, num[1], operators[operator_index])
            operator_index += 1
    print(result)