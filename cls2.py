# class complex():
#     def __init__(self,real,imag):
#         self.real=real
#         self.imag=imag
#     def add(self,number):
#         real=self.real+number.real
#         imag=self.imag+number.imag
#         result=complex(real,imag)
#         return result
#
# n1=complex(-2,4)
# n2=complex(6,7)
# result=n1.add(n2)
#
# print("real",result.real)
# print("imag",result.imag)



class triangle():
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def get_perimeter(self):
        perimeter=self.a+self.b+self.c
        return perimeter

t1=triangle(8,9,2)
perimeter=t1.get_perimeter()
print("The perimeter of t1 triangle is", perimeter)


