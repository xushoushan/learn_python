# -*- coding: utf-8 -*-
# def fact(n):
#     if n==1:
#         return 1
#     return n*fact(n-1)

# print(fact(1))
# print(fact(5))
# print(fact(1000))

#尾递归
def fact(n):
    return fact_iter(n,1)
def fact_iter(num,product):
    if num==1:
        return product
    return fact_iter(num-1,num*product)
print(fact(5))

#汉诺塔
# 当N>=2时，我们想要把所有的盘从A通过B移到C，那么需要先把A上面N-1个盘通过C转移到B，
#再把最下面的那个最大的盘(1个)从A直接转移到C，然后再把B上面的所有盘（n-1个）通过A转移到C。
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
move(4, 'A', 'B', 'C')