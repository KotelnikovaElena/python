num = int(input('Введите целое положительное число='))
num_ost = num % 10
num = num // 10
while num > 0:
    if num % 10 > num_ost:
        num_ost = num % 10
    num = num // 10
print('Наибольшая цифра в числе=', num_ost)
