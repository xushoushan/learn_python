# -*- coding: utf-8 -*-
import animals
import types

a=animals.Animal()
print(type(123))
print(type('str'))
print(type(None))
print(type(abs))
print(type(a))

def fn():
    pass

print(type(123)==type(456))
print(type(123)==int)
print(type(fn)==types.FunctionType)

#isinstance
d=animals.Dog()
print(isinstance(d,animals.Dog) and isinstance(d,animals.Animal))

print(isinstance([1, 2, 3], (list, tuple)))

print(dir('ABC'))

class MyDog(object):
    def __len__(self):
        return 100

dog=MyDog()
print(len(dog))

#配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
class MyObject(object):
    def __init__(self):
        self.x=9
    def power(self):
        return self.x * self.x
obj=MyObject()
print(hasattr(obj,'x'))
print(obj.x)
print(hasattr(obj,'y'))
setattr(obj,'y',19)
print(hasattr(obj,'y'))
print(obj.y)
getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404

fn = getattr(obj,'power')
print(fn())
sum = obj.x + obj.y


def readImage(fp):
    if hasattr(fp, 'read'):
        return read(fp)
    return None

