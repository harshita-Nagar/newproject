# a=4
# b=5
# print(a+b)

# print(int.__add__(a,b))

# class Student:
#     def __init__(self,m1,m2):
#         self.m1=m1
#         self.m2=m2
#     def __add__(self, other):
#         m1=self.m1+other.m1
#         m2=self.m2+other.m2
#         S3=Student(m1,m2)
#
#         return S3


    # def __gt__(self, other):
    #     r1=self.m1+self.m2
    #     r2=other.m1+other.m2
    #     if r1>r2:
    #         return True
    #     else:
    #         return False



# class A:
#     def __init__(self,a):
#         self.a=a
#     def __add__(self,o):
#         return self.a+ o.a
#
# obj1=A(1)
# obj2=A(3)
# obj3=A("fun")
# obj4=A("enjoy")
#
# print(obj1+obj2)
# print(obj3+obj4)


class A:
    def __init__(self,a):
        self.a=a
    def __gt__(self,other):
        if self.a>other.a:
            return True
        else:
            return False

Obj1=A(3)
Obj2=A(6)

if (Obj1>Obj2):
    print("Obj1 is greater than Obj2")
else:
    print("Obj2 is greater than Obj1")
