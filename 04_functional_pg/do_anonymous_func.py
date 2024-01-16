# -*- coding: utf-8 -*-
L = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(L)
def f(x):
    return x * x

f=lambda x: x * x
print(f)
print(f(19))
def build(x,y):
    return lambda: x * x + y * y
print(build(3,5)())
print(build(3,5))

# def is_odd(n):
#     return n % 2 == 1

# L = list(filter(is_odd, range(1, 20)))
# print(L)

def is_odd(n):
    return n % 2 == 1

L = list(filter(lambda x : x%2==1, range(1, 20)))
print(L)