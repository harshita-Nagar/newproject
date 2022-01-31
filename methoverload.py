def product(a,b):
    p=a*b
    print(p)

def product(a,b,c):
    p=a*b*c
    print(p)

product(2,4) # only works with the latest method

# class Student:
#     def __init__(self,m1,m2):
#         self.m1=m1
#         self.m2=m2
#     def sum(self,a,b,c):
#         s=a+b+c
#         return s
#
# s1=Student()

# print(s1.sum(2,3)) print an error

# to solve this problem

class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def sum(self,a=None,b=None,c=None):
        s=a+b+c
        return 0
    if a!=None and b!=None and c!=None:
        s=a+b+c
