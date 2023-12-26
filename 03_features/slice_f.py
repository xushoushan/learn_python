# -*- coding: utf-8 -*-
L=[]
n=1
while n<=99:
    L.append(n)
    n=n+2

r=[]
n=3
for i in range(n):
    r.append(L[i])
print(r)

print(L[0:3])
print(L[:10])
print(L[1:3])
print(L[-2:])
print(L[-2:-1])
print(L[:10:2])
print(L[::5])
print((0, 1, 2, 3, 4, 5)[:3])

#利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(s):
    while s and s[0].isspace():
        s = s[1:]
    while s and s[-1].isspace():
        s = s[:-1]
    return s
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

#思路一，把空格切掉：
def trim(s):
    while s != '' and s[0] == ' ':
        s = s[1:]
    while s != '' and s[-1] == ' ':
        s = s[:-2]

    return s
#思路二，把非空格字符提取出来：
def trim(s):
    length = len(s)
    left = 0
    right = length - 1
    
    while length > left and s[left] == ' ' :
        left = left + 1
    
    while right > 0 and s[right] == ' ' :
        right = right - 1
    
    return s[left:right+1]