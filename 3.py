
arg_1 = float(input('Введите первое число: '))
arg_2 = float(input('Введите второе число: '))
arg_3 = float(input('Введите третье число: '))


def my_func():

    if arg_1 >= arg_3 and arg_2 >= arg_3:
        return arg_1 + arg_2
    elif arg_2 >= arg_1 and arg_3 >= arg_1:
        return arg_2 + arg_3

    else:
        return arg_3 + arg_1


my_result = my_func()
print(my_result)
