my_list = [300, 2, 2, 44, 1, 1, 4, 1, 7, 1, 7, 55, 55]
new_list = [el for el in my_list if my_list.count(el) < 2]
print(f'Исходный список: {my_list}')
print(f'Новый список: {new_list}')
