my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for index, el in enumerate(my_list) if my_list[index - 1] < my_list[index]]
print(f'Исходный список: {my_list}')
print(f'Новый список: {new_list}')
