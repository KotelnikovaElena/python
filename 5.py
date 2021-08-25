from random import randint


with open("text_5.txt", 'w+', encoding='utf-8') as f_obj:

    for line in range(100):
        f_obj.write(str(randint(1, 15)) + " ")
    f_obj.seek(0)
    print(sum(map(int, f_obj.readline().split())))
