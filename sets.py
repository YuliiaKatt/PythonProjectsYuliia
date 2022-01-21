import random

set_1 = {random.randint(0, 10) for i in range(3)}
print("Множество 1: ", set_1)

set_2 = {random.randint(0, 10) for j in range(10)}
print("Множество 2: ", set_2)

if set_1 <= set_2:
    print("True! Множество 1 является суперсетом для множества 2")
else:
    print("False! Множество 1 не является суперсетом для множества 2")
