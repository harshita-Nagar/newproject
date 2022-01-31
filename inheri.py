# class Animal:
#     def eat(self):
#         print("I can eat")
#
#
# class Dog(Animal):
#     def bark(self):
#         print("dogs bark at strangers")
#
# d1=Dog()
# d1.bark()
# d1.eat()
#
#
# class Cat(Animal):
#     def meow(self):
#         print("cat says meow")
#
# c1=Cat()
# c1.meow()
# c1.eat()

class A:
    def __init__(self,a_name):
        self.a_name=a_name


class B(A):
    def __init__(self,b_name,a_name):
        self.b_name=b_name
        A.__init__(self,a_name)


class C(B):
    def __init__(self,c_name,b_name,a_name):
        self.c_name=c_name
        B.__init__(self,b_name,a_name)

        def display_name(self):
            print("A name", self.a_name)
            # print("B name", self.b_name)
            # print("C name", self.c_name)


obj_1=A("child class","intermidiate class","parent class")
# print(obj_1.a_name)
obj_1.display_name()