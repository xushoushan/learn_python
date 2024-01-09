# -*- coding: utf-8 -*-
def f(x):
    return x*x
r=map(f,[1,2,3,4,5,6,7])
print(r)
print(list(r))

from functools import reduce
def add(x,y):
    return x+y
print(reduce(add,[1,3,4,5,6]))

def fn(x,y):
    return x*10 + y
def char2num(s):
    digits={'0':0,'1':1,'2':2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

print(reduce(fn,map(char2num,'986193')))
def str2int(s):
    def fn(x,y):
        return x*10 + y
    def char2num(s):
        digits={'0':0,'1':1,'2':2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[s]
    return reduce(fn,map(char2num,s))
print(str2int('89087'))

def str2int_lambda(s):
    digits={'0':0,'1':1,'2':2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def char2num(s):
        return digits[s]
    return reduce(lambda x,y: x*10 + y,map(char2num,s))
print(str2int_lambda('134578'))

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    transformed_word = name[0].upper() + name[1:].lower()
    return transformed_word
    #return name.title()
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    return reduce(lambda x,y: x * y,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')