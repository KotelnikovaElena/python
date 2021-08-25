dict_list = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_list = []
with open("text_4.txt", 'r', encoding='utf-8') as f_obj:
    for i in f_obj:
        i = i.split(' ', 1)
        new_list.append(dict_list[i[0]] + ' ' + i[1])
    print(new_list)

with open("new_text_4.txt", 'w') as new_obj:
    new_obj.writelines(new_list)
