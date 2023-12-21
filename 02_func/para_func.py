# -*- coding: utf-8 -*-

# def power(x, n=2):
#     s=1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s


# print(power(5,3))

# def calc(numbers):
#     sum=0
#     for n in numbers:
#         sum=sum+n*n
#     return sum

# print(calc([1,2,3]))

#可变参数
# def calc(*numbers):
#     sum=0
#     for n in numbers:
#         sum=sum+n*n
#     return sum

# print(calc(1,2,3,5))
# nums=[1,3,5]
# print(calc(*nums))

#关键字参数
# def person(name, age, **kw):
#     if 'city' in kw:
#         pass
#     print('name:',name,'age:','other:',kw)
# person('Michael',30)
# person('Bob',33,city='Beijing')
# person('Adam',38,gender='M',job='Engineer')

# extra={'city':'Beijing','Job':'Engineer'}
# person('Jack',24,**extra)

#命名关键字参数
# def person(name,age,*,city,job):
#     print(name,age,city,job)
#person('Jack', 24, city='Beijing', job='Engineer')
# person('Jack', 24, 'Beijing', job='Engineer') #error
def person(name,age,*args,city,job):
    print(name,age,city,job)
    print(args)
person('Jack', 24, 'AAA','BBB',city='Beijing', job='Engineer') #error

#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
#对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

#以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
def mul(y,*x):
    for x1 in x:
        y=  y * x1
    return y
# 测试
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('测试失败!')
elif mul(5, 6) != 30:
    print('测试失败!')
elif mul(5, 6, 7) != 210:
    print('测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        mul()
        print('测试失败!')
    except TypeError:
        print('测试成功!')