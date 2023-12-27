# -*- coding: utf-8 -*-
from collections.abc import Iterable
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

from collections.abc import Iterator
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))

#iter()
print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))

# 凡是可作用于for循环的对象都是Iterable类型
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象

for x in [1, 2, 3, 4, 5]:
    pass
#等价于
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
    