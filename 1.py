def get_div_func():
    try:
        result = num_1() / num_2()
        return result
    except ZeroDivisionError:
        print('Ошибка. На ноль делить нельзя!')


def num_1():
    a = float(input('Введите первое число: '))
    return a


def num_2():
    b = float(input('Введите второе число: '))
    return b


get_div = get_div_func()
print(get_div)
