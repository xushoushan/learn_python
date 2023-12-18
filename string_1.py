#print('I\'m ok.')
#print('\\\t\\')
# print('''line1
# ...line2 \n
# ...     33d.  line3
# ''')
# print(r'''line1
# ...line2 \n
# ...     33d.  line3
# ''')
# print(3>2)
# print(ord('A'))
# print(chr(20013))
# print('\u4e2d\u6587')
# print('Hello world')
# print('Hello, %s' % 'Mike')
# print('Hello, %s, you have earned $%d.' % ('Mike',200000))
# 占位符	替换内容
# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数
#格式化整数和浮点数还可以指定是否补0和整数与小数的位数：
# print('%2d-%04d' % (3, 1))
# print('%.4f' % 3.1415926)
# print('growth rate: %d %%.' % 20)
# print('hello, {0}, you get a {1:.2f} % growth'.format('Mike',21.123))
r=2.5
s=3.14*r**2
print(f'The area of a circle with radius {r} is {s:.2f}')
s1=72
s2=85
r=s2/s1-1
print('%.5f' % r)