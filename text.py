# a = 4
# b = 5
# if a > b:
#  print("a is greater than b")
# else:
#  print("b is greater than a")
#
#
# number ={1,2,3,4,5}
# for i in number:
#     print(i)
#
# for i in range(10):
#  print(i)


# for i in range(10):
#  print(i)
# else:
#  print("done")
#
# def add(a,b):
#     return a+b
#
# print(add(4,5))


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name,self.age)

p1 = Person("John", 36)
p1.display()
p2 = Person("Jane", 32)
p2.display()
