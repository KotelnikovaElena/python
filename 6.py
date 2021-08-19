from itertools import count
from itertools import cycle

for el in count(int(input('Введите стартовое число: '))):
    if el <= 10:
        print(el)
    else:
        break


count = 0
my_list = ['Mama', 'ABC', 123, True]
for el in cycle(my_list):
    if count == 10:
        break
    count += 1
    print(el)
