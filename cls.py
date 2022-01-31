#
# # class Person:
# #   def __init__(self, name, age):
# #       self.name=name
# #       self.age=age
# # p1=Person("john",87)
# # print(p1.name)
# # print(p1.age)
#
#
# # class Person:
# #   def __init__(self, name, age):
# #     self.name = name
# #     self.age = age
# #
# # p1 = Person("John", 36)
# #
# # print(p1.name)
# # print(p1.age)
#
#
# # class Person:
# #     def __init__(self,name,age):
# #         self.name=name
# #         self.age=age
# #     def my_func(self):
# #         print("Hello my name is " + self.name  +   "and my age is" +   self.age)
# # P1 = Person ("harshita" ,"45")
# # P1.my_func()
#
#
# # P1.age=23
# # print(P1)
#
# # class students():
# #     def check_pass_fail(self):
# #         if self.marks>=40:
# #             return True
# #         else:
# #             return False
# # student1=students()
# # student1.name="Harry"
# # student1.marks=89
# #
# # did_pass=student1.check_pass_fail()
# # print(did_pass)
#
#
# # class students():
# #     def check_pass_fail(self):
# #         if self.marks>=40:
# #             return True
# #         else:
# #             return False
# #     def __init__(self,name,marks):
# #         self.name=name
# #         self.marks=marks
# #  student1=students("vani",34)
# # student2=students("sahil",56)
# # print(student1.name)
# # print(student1.marks)
# # print(student2.name)
# # print(student2.marks)
#
# # did_pass=student1.check_pass_fail()
# # print(did_pass)
# # did_pass=student2.check_pass_fail()
# # print(did_pass)
#
#
# class employee():
#     def __init__(self,name,age,post):
#         self.name=name
#         self.age=age
#         self.post=post
# employee1=employee("Heeru",54,"salesman")
# employee2=employee("Teenu",65,"tester")
# employee3=employee("Yash",83,"BA")
# # print(employee1.name)
# # print(employee2.name)
# # print(employee3.name)
# employee1.salary=50000
# print(employee1.__dict__)
#
#
# class Dog():
#
#     attri="Nannok"   # class attribute
#
#     def __init__(self,name):
#         self.name=name  # instance attribute
#
#
# dog1=Dog("Cuddle")
# dog2=Dog("Marry")   # object instantiation
#
# print("my friend is {}". format(dog1. __class__. attri))
# print("my friend is {}". format(dog2. __class__. attri))   # accessing class attributes
#
# print("my name is {}".format(dog1.name))
# print("my name is {}".format(dog2.name))
#
#
# class Person():
#
#     def __init__(self,name,idnumber):
#         self.name=name
#         self.idnumber=idnumber
#
#     def details(self):
#         print(self.name)
#         print(self.idnumber)
#
#     def Show(self):
#         print("His name is",{}.format(self.name))
#         print("His idnumber is",{}.format(self.idnumber))
#
#
# class Employee(Person):
#     def __init__(self,name,idnumber,post,salary):
#         self.post=post
#         self.salary=salary
#
#
#     Person. __init__(self,name,idnumber)
#
#     Person.__init__(self, name, idnumber)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
from abc import ABC

class Shape:
    def __init__(self,a,b):
        self.a=a
        self.b=b


class Rectangle(Shape):
    def calculate_area(self):
        return self.a*self.b

Area=Rectangle(5,6)
print(Area.calculate_area())