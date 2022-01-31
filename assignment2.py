class Student:
    def __init__(self,name, id, age):
        self.name=name
        self.id=id
        self.age=age

        def details(self):
            print("Student name is", self.name, "id is", self.id, "and age is", self.age)


s1 = Student("Varun", 1, 12)
s2 = Student("Veronika", 2, 14)

s1.Student()

# print(s1.details())