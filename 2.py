my_list = input('Введите элементы списка:').split()
for a in range(0, len(my_list)-1, 2):
    my_list[a], my_list[a + 1] = my_list[a + 1], my_list[a]
print(my_list)
