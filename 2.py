def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func(name='Василий', surname='Пупкин;', year='1990;', city='Санкт-Петербург;', email='pupkin@mail.ru;',
              telephone='89111234567'))
