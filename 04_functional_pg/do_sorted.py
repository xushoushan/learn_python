# -*- coding: utf-8 -*-
# print(sorted([36,2,-44,7,112]))
# print(sorted([36,2,-44,7,112],key=abs))
# print(sorted(['bob', 'about', 'Zoo', 'Credit']))
# print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#请用sorted()对上述列表分别按名字排序：
def by_name(t):
    return t[0].lower()
def by_score(t):
    return -t[1]
L2 = sorted(L, key=by_name)
print(L2)
L3 = sorted(L, key=by_score)
print(L3)
