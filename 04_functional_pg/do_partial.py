# -*- coding: utf-8 -*-
int('12345')

# def int2(x, base=2):
#     return int(x, base)

# print(int2('10101010011'))

import functools
int2=functools.partial(int,base=2)
print(int2('10101010011'))

kw={'base':2}
int('11001',**kw)

max2=functools.partial(max,10)
#实际上会把10作为*args的一部分自动加到左边，也就是：
max2(5,6,7)
#相当于
args=(10,5,6,7)
max(*args)

#偏函数可以简化参数操作。
#当函数的某个参数是我们可以提前获知的，那我们就可以将它固定住！
# 定义一个取余函数，默认和2取余；
def mod(x,y=2):
  # 返回 True 或 False
  return x % y == 0

# 假设我们要计算和3取余，如果不使用partial()函数，那么我们每次调用mod()函数时，都要写y=3
mod(4,y=3)
mod(6,y=3)

# 使用partial()函数
from functools import partial
mod_3 = partial(mod,y=3)
mod_3(4)
mod_3(6)

