

numbers = ['1', '2', '3', '4', '5', '6', '7']

""" Реализация через reversed """

rv_numbers = iter(reversed(numbers))
print(next(rv_numbers))
print(next(rv_numbers))
print(next(rv_numbers))
print(next(rv_numbers))
print(next(rv_numbers))
print(next(rv_numbers))
print(next(rv_numbers))
print(next(rv_numbers))
print(type(rv_numbers))


#____________________________

def reverse_iter(x):
    """ Реализация через yield """
    n = 10
    while n > x:     
        yield n
        n -= 1
z = reverse_iter(0)
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))