# -*- coding: utf-8 -*-

# print(list(range(1,11)))
# L=[]
# for x in range(1,11):
#     L.append(x*x)
# print(L)

# print([x*x for x in range(1,11)])
# print([x*x for x in range(1,11) if x%2==0])

# print([m+n for m in 'ABCD' for n in 'XYZ'])

import os
print([d for d in os.listdir('.')]) # os.listdir可以列出文件和目录

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

#在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else。
L1=[x for x in range(1, 11) if x % 2 == 0]
L2=[x if x % 2 == 0 else -x for x in range(1, 11)]
print(L1,L2)

#请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')