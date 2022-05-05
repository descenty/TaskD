import math
from math import *


def k_func(x: float, y: float, a: float, k: float):
    try:
        value = abs(cos(x**2 + (44 * pi) / 180) + a * sin(k * y) ** 2)
        value -= 0.6 * (y**3)
        value += log2(8) / (4 * a)
        return value
    except ZeroDivisionError:
        print("ДЕЛЕНИЕ НА НОЛЬ")
    return None


def b_func(x: float, y: float):
    try:
        return e**(abs(4 * y - 0.5)) + sqrt(x**(1/3)) / (1 + log(2 * x, e))
    except ZeroDivisionError:
        print('ДЕЛЕНИЕ НА НОЛЬ')
    return None


# тестирование функций
print('k =', k_func(x=1, y=1, a=1, k=1))
print('B =', b_func(x=1, y=1))
