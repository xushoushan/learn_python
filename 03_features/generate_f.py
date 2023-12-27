# -*- coding: utf-8 -*-
# L=[x*x for x in range(10)]
# print(L)
# g=(x*x for x in range(10))
# print(g)
# # print(next(g))
# # print(next(g))
# print('------')
# for n in g:
#     print(n)

# def fib(max):
#     n,a,b=0,0,1
#     while n<max:
#         print(b)
#         a,b=b,a+b
#         n=n+1
#     return 'done'
# print(fib(10))
# print(fib(2))

#a,b=b,a+b
        #相当于
# t = (b, a + b) # t是一个tuple
# a = t[0]
# b = t[1]

#generator函数
# def fib(max):
#     n,a,b=0,0,1
#     while n<max:
#         #print(b)
#         yield b
#         a,b=b,a+b
#         n=n+1
#     return 'done'
# f=fib(6)
# print([x for x in f])

# g=fib(6)
# while True:
#     try:
#         x=next(g)
#         print('g:',x)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break

# def odd():
#     print('step 1')
#     yield 1 
#     print('step 2')
#     yield(3)
#     print('step 3')
#     yield(5)

# o=odd()
# print(next(o))
# print(next(o))
# print(next(o))
# print(next(o))

def triangles():
    L2=[1]
    while True:
        yield L2
        L1=[1]
        for n in range(len(L2)-1):
            L1.append(L2[n]+L2[n+1])
        L1.append(1)
        L2=L1
#list指针关系，如果一直修改L2并返回L2，最后测试case中每个list都是10个元素。
#下方为chatGPT生成的代码
# def triangles():
#     row = [1]
#     while True:
#         yield row
#         row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]

# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')


