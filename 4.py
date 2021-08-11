words = input('Введите слова через пробел: ')
number = 1
my_words = []
if words.isdigit() is False:
    for word in range(words.count('') + 1):
        my_words = words.split()
        if len(str(my_words)) <= 10:
            print(f'{number} {my_words [word]}')
            number += 1
        else:
 #           print(f'{number} {my_words [word]}')
            number += 1
print('Проверьте слова, вы ввели их с ошибкой')
