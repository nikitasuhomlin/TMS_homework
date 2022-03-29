# Burger decorator 

def burger_decoration(func):
    def burger_decorator(*args):
        print("помидоры ", "котлета")
        func(*args)
        
    return burger_decorator

@burger_decoration
def ingredients(something):
    print(something)

ingredients("салат, булка")

#______________________________________________________________

# Countdown to pizzatime

import time 

def microwave(x):
    """ Функции обратного отсчёта
    времени"""
    while x:
        mins = x // 60
        secs = x % 60
        timer = "{:02d}:{:02d}".format(mins, secs)
        print(timer)
        time.sleep(0.9)
        x -= 1
        
x = input("Начальное число отсчёта:")
microwave(int(x))
print("Pizza time!")

#____________________________________________________

# MAP FILTER REDUDE
# 1

# Дробное => Целое

import math 

circle_areas = [6.56773, 9.57668,
4.00914, 56.24241, 9.01344,
32.00013]

result = list(map(round, circle_areas, range(1,7)))

print(result)

#__________________________________________________

# Пансионат (люди, которые > 80, используя 
# filter)

ages = [66, 90, 68, 59, 
76, 60, 88, 74, 81, 65, 92, 85] 

def person(age):
    return age > 80

over_80 = list(filter(person, ages))

print(over_80)

#__________________________________________________

# Фильтрация слов палиндромов из списка

values = ['demigod', 'rewire', 'madam',
'fortran', 'xamarin','salas','PHP']

palindromes = list(filter(lambda word:
 word == word[::-1], values))

print(palindromes)

#_________________________________________________

# Произведение чисел из списка, используя reduce
from functools import reduce

numbers = [1, 2, 3, 4]

def multiplication(first, second):
    return first * second

result = reduce(multiplication, numbers)

print(result)

#_______________________________________________

# Возвращает большое число из списка:
from functools import reduce
values = [3, 5, 2, 4, 7, 1]

print(reduce(max, values))

#_______________________________________________

# Количество слова Капитан в списке

sentences = ['капитан джек воробей',
'капитан дальнего плавания',
'ваша лодка готова, капитан']







