# -*- coding: utf-8 -*-
d={'a':1, 'b':2, 'c':3}
for key in d:
    print(key)

for value in d.values():
    print(value)

for k,v in d.items():
    print(k,v)

for ch in 'ABC':
    print(ch)

from collections.abc import Iterable
print(isinstance('abc', Iterable))
print(isinstance([1,2,3], Iterable))
print(isinstance(123, Iterable))

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1,'a'), (2,'b'), (3,'c')]:
    print(x,y)

#请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    min=None
    max=None
    for i,v in enumerate(L):
        if i == 0:
            min=v
            max=v
        else:
            if min>v:
                min=v
            if max<v:
                max=v  
    return (min, max)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

#
#     if not isinstance(L, Iterable):
# raise TypeError('类型错误，不可迭代')
    # 	if len(L) == 0:
	# 	return(None,None)
	# else: 
	# 	max = L[0]
	# 	min = L[0]
	# 	for i in L:
	# 		if i > max:
	# 			max = i
	# 		elif i < min:
	# 			min = i
	# 	return (min,max)