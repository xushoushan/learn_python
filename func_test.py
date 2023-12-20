# -*- coding: utf-8 -*-
# from abs_test import my_abs
# print(my_abs(-102))

# def nop():
#     pass

# age = 10
# if age >= 18:
#     pass

# import math
# def move(x, y, step, angle=0):
#     nx=x+step*math.cos(angle)
#     ny=y-step*math.sin(angle)
#     return nx, ny

# x,y =move(100,100,5,math.pi/3)
# print(math.sin(math.pi/2))
# print(math.cos(math.pi/2))
# print(x,y)

# r =move(100,100,60,math.pi/6)
# print(r)

#
import math

def quadratic(a, b, c):
    for i in [a, b, c]:
        if not (isinstance(i, int) or isinstance(i, float)):
            raise TypeError(f"bad operand type for quadratic(): '{type(i)}'")
    x1=(-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    x2=(-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    return (x1,x2)
# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')