# -*- coding: utf-8 -*-
# def is_odd(n):
#     return n%2==1
# print(list(filter(is_odd,[1,2,3,4,5,6,7,8,11,33,22])))

# def not_empty(s):
#     return s and s.strip()
# print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  ','d d',' e '])))
# # 结果: ['A', 'B', 'C']

# def _odd_iter():
#     n=1
#     while True:
#         n=n+2
#         yield n

# def _not_divisible(n):
#     return lambda x:x%n>0
# def primes():
#     yield 2
#     it =_odd_iter()
#     while True:
#         n=next(it)
#         yield n
#         it=filter(_not_divisible(n),it)

# for n in primes():
#     if n<1000:
#         print(n)
#     else:
#         break

def is_palindrome(num):
    # num_str=str(n)
    # reversed_str = num_str[::-1]
    # return num_str == reversed_str
    if num < 0:
        return False  # 负数不是回文数
    original_num = num
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return original_num == reversed_num
    # reversed_str=[]
    # for n in str(n):
    #     reversed_str.append(n)
    # for n in range(len(str(n))):
    #     reversed_str[-int(n)-1]=n
    # return str(n) == reversed_str
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')