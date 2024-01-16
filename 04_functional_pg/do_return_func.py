# -*- coding: utf-8 -*-
def calc_sum(*args):
    ax=0
    for n in args:
        ax=ax+n
    return ax

def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum

f=lazy_sum(1,3,4,5,6,10)
print(f)
print(f())

#请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
# >>> f1 = lazy_sum(1, 3, 5, 7, 9)
# >>> f2 = lazy_sum(1, 3, 5, 7, 9)
# >>> f1==f2
# False

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(),f2(),f3())
#全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
#返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

def countx():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1, f2, f3 = countx()
print(f1(),f2(),f3())

#利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    x=0
    def counter():
        nonlocal x
        x=x+1
        return x
    return counter
# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')