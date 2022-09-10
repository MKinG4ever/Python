import random
import sys
from random import random as rnd
from time import sleep as dly

squares = [x ** 2 for x in range(10)]

a = [i for i in range(10)]
aa = [i for i in range(10) if i > 5]
aaa = [i for i in range(10) if i > 5 in range(4)]

b = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]

b_compact = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            b_compact.append((x, y))

c = [i for i in "Hello World."]  # output is a list

d = {i for i in "Hello World."}  # output is a set

h = 'A' if 5 > 10 else 'B'

e = ['Hi' for _ in range(5)]

f = [no for no in range(100) if True]

g = [n if 5 > 2 else n - 1 for n in list(range(1, 10))]

q = [(a, b) if 5 > 2 else (b, a) for a in range(5, 15) for b in range(10, 20)]

h = ['TRUE' if 2 > 5 else 'FALSE']

m = [[j for j in range(i)] for i in range(6)]

w = [[j for j in range(i, i + 5, 2)] for i in range(6)]

###

no1 = 'A' if False else 'B'

no2 = 'A' if False else 'B' if False else 'C'

no3 = 'A' if False else 'B' if False else 'C' if True else 'D'

no4 = ['A' if False else 'B' if False else 'C' if True else 'D' for i in range(5)]

no5 = ['A' for i in range(5)]

no6 = [('A', i) for i in range(5)]

no7 = [(x, y) for x in range(10, 20) for y in range(30, 40)]

###
for x in range(10) if False else range(15):
    print(x)
###

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

k = [[row[i] for row in matrix] for i in range(4)]

r = zip(range(110), [rnd() for _ in range(110)])
t = list(r)

"""
str -> str(""Chr) / "Chr"

int,float,complex
    int(3) / 3
    float(3.141592) / 3.141592
    complex(3j) / 3j

bool -> True or False

list,tuple,range
    list((1,2,'3','Hi')) / [1,2,3,'Hi']
    tuple((1,2,3,'Hi')) / (1,2,3,'Hi')
    range(1:10:2) -> start:stop:step

set,frozenset
    set((1,2,3,4,5,6)) / {1,2,3,4,5,6,}
    frozenset((1,2,3,4,5,6))

dict -> dict(name="John", age=36) / {"name" : "John", "age" : 36}

None -> None

bytes,bytearray,memory_view
    b"Hello" / bytes("Hello")  # ( r"RAW", b"bytes", f"format" )
    bytearray(5)
    memoryview(bytes(5))
"""
