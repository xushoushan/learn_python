# -*- coding: utf-8 -*-
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Eating meat...')
class Cat(Animal):
    pass

dog=Dog()
dog.run()
dog.eat()

cat=Cat()
cat.run()


a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型

print(isinstance(a,list))
print(isinstance(b,Animal))
print(isinstance(b,Dog))
print(isinstance(c,Dog))
print(isinstance(c,Animal))

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())