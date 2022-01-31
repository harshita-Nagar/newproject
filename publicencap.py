# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#
#     def Show(self):
#         print("Name:", self.name, "Salary:", self.salary)
#
# emp=Employee("Mokshita", 45000)
#
# print("Name:", emp.name, "Salary:", emp.salary)
#
# emp.Show()
#This is example of public member in encapsulation.

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary  # private member
#
#
# emp = Employee("Mokshita", 45000)
# print("Salary:", emp.__salary) # will give an error because we can't access a private member.


# direct access to private member using name mangling
# print('Salary:', emp._Employee__salary)

# protected member

# class Company:
#     def __init__(self):
#         self._project=game
#
#
# class Employee(Company):
#     def __init__(self):
#         self.name=name
#         Company.__init__(self)
#
#         def Show(self):
#             print("Employee Name:", self.name)
#             print("working on project:", self._project)

# c=Employee("Juhi")
# c.Show()
#
# print("Project:", c._project )



class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def Show(self):
        print("Name:", self.name, "Salary:", self.salary)


emp=Employee("Jessica", 78000)
print("Name:", emp.name, "Salary:", emp.salary)

# emp.Show()
