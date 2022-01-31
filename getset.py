class Student:
    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age


s=Student("Vanshika", 2, 12)
print(getattr(s, "name"))

print(setattr(s,"name", "Veronika"))

print(getattr(s,"name"))
