def my_sum():
    sum_res = 0
    ex = False
    while ex is False:
        number = input('Введите число или Q, чтобы выйти: ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q' or number[el] == 'й' or number[el] == 'Й':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Текущая сумма: {sum_res}')
    print(f'Финальная сумма: {sum_res}')


my_sum()
