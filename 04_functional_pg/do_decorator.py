# -*- coding: utf-8 -*-
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} 执行时间: {execution_time:.6f} 秒")
        return result
    return wrapper

# 使用装饰器
@timing_decorator
def example_function():
    # 这里可以是任何需要测量执行时间的函数体
    time.sleep(2)
    print("Function executed!")

# 调用带有装饰器的函数
example_function()


# def log_decorator(arg=None):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             print('begin call')
#             if arg:
#                 print(arg)
#             result = func(*args, **kwargs)
#             print('end call')
#             return result
#         return wrapper
#     return decorator

# # 使用 @log 装饰器
# @log_decorator
# def example_function1():
#     print("Function 1 executed!")

# @log_decorator('execute')
# def example_function2():
#     print("Function 2 executed!")

# # 调用带有装饰器的函数
# example_function1()
# example_function2()
import functools
def log_decorator(arg=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('begin call')
            if arg:
                print(arg)
            result = func(*args, **kwargs)
            print('end call')
            return result
        return wrapper

    # 如果装饰器被调用时带有参数，直接返回 decorator
    if callable(arg):
        return decorator(arg)

    # 否则返回装饰器函数
    return decorator

# 使用 @log 装饰器
@log_decorator
def example_function1():
    print("Function 1 executed!")

@log_decorator('execute')
def example_function2():
    print("Function 2 executed!")

# 调用带有装饰器的函数
example_function1()
example_function2()


import time, functools
def metric(fn):
    @functools.wraps(fn)
    def wr(*args, **kw):
        st = time.time()
        f=fn(*args, **kw)
        et = time.time()
        print('%s executed in %.6f ms' % (fn.__name__, et - st))
        return f
    return wr
# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')