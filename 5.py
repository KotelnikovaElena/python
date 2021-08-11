my_list = [9, 5, 4, 4, 2, 1, 0]
new_element = input('Введите новый элемент: ')
if new_element.isdigit() is True:
    new_element = int(new_element)
    my_list.append(new_element)
    my_list.sort(reverse=True)
    print(my_list)
else:
    print('Ошибка')