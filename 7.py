from itertools import count
from math import factorial


def generator():
    for el in count(1):
        yield factorial(el)


gen = generator()

n = 0
for i in gen:
    if n < 15:
        print(i)
        n += 1
    else:
        break
