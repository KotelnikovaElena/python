seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
numbers = input('Введите число от 1 до 12: ')
if numbers.isdigit() is True:
    numbers = int(numbers)
    if numbers == 12 or numbers == 1 or numbers == 2:
        print(seasons_dict.get(1))
        print(seasons_list[0])
    elif numbers == 3 or numbers == 4 or numbers == 5:
        print(seasons_dict.get(2))
        print(seasons_list[1])
    elif numbers == 6 or numbers == 7 or numbers == 8:
        print(seasons_dict.get(3))
        print(seasons_list[2])
    elif numbers == 9 or numbers == 10 or numbers == 11:
        print(seasons_dict.get(4))
        print(seasons_list[3])
    else:
        print('Месяца под таким номером не существует')

else:
    print('Ошибка, Вы ввели не число')
