from abc import ABC


class Shape: # abstract class
    def calculate_area(self):  # no implementation
        pass


class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def calculate_area(self):
        return self.length * self.breadth


class Triangle(Shape):
    def __init__(self,a,b):
        self.a=a
        self.b=b
        # self.c=c

    def calculate_area(self):
        # s=(self.a+self.b+self.c)/2
        # return (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
        return (self.a * self.b)**0.5

Area1=Rectangle(6,8)
Area2=Triangle(8,2)

print(Area1.calculate_area())
print(Area2.calculate_area())

from abc import ABC, abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):
    def process(self):
        print("it's running")
com1=Laptop()
com1.process()

