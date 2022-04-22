# 1) Создать калькулятор
# 2) Обернуть его в try / except
# 3) Сделать своё исключение
# и подключить его к try / except 

# calc v1

from decimal import DivisionByZero


a = 45  #  Первое число
b = 25  #  Второе число
c = 0   #  Третье число
result = 0 # Результат


class MyException:
    def calc(self, act):
        if act == 1:
            result = a + b
        elif act == 2:
            result = a - b 
        elif act == 3:
            result = a * b
        elif act == 4:
            result = a / b
        elif act == 5:
            result = a / c
        elif act == 6:
            result = b / c
        elif act == 7:
            result = a + c / b
        elif act == 8:
            result = a + b / c
        
        return result

test = MyException()

for x in range(1,8):
    try:
        result = test.calc(x)
        print(x,'.' + ' = ', result)
    except ZeroDivisionError as eror:
        print(' На ноль делить нельзя!')

#____________________________________________

# calc v2

first_number = float(input('Введите первое число: '))
calc = input('Какую операцию будем выполнять? ')
second_number = float(input('Введите второе число: '))
if calc == '+':
    print(first_number + second_number)
elif calc == '-':
    print(first_number + second_number)
elif calc == '/':
    try:
        print(first_number / second_number)
    except ZeroDivisionError as Error:
        print(' На ноль делить нельзя!')
    except ValueError as Error:
        print('Это калькулятор, а не словарь!')

elif calc == '*':
    print(first_number * second_number)






