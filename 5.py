from functools import reduce


def my_func(el_f, el):

    return el_f * el


print(f'Список четных значений {[el for el in range(100, 1001) if el % 2 == 0]}')

print(f'Произведение: {reduce(my_func, [el for el in range(100, 1001) if el % 2 == 0])}')
