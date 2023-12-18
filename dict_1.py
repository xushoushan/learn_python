#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# d = {'Michael':95,'Bob':75,'Tracy':85}
# print(d['Bob'])
# d['Adam']=66
# print(d)
# print('Tom' in d)
# print(d.get('Tom'))
# d.pop('Bob')
# print(d)

# s = set([1,2,3,4,1])
# print(s)
# s.remove(4)
# print(s)
# s.add(5)
# print(s)

# s1 = set([1, 2, 3])
# s2 = set([2, 3, 4])
# print(s1 & s2)
# print('s1 | s2:' + str(s1|s2))

s1 = set((1, 2, 3))
print(s1)
#set需要不可变对象作为key，list会报错
s2 = set((1, [2, 3]))
print(s2)