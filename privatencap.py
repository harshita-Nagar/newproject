# Private member

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.__salary=salary
#
#     def Show(self):
#         print("Name:", self.name, "Salary:", self.__salary)
#
#
# emp = Employee("Jessica", 78000)
# print("Name:", emp.name, "Salary:", emp.__salary)
#
# emp.Show() # will g ive an error. below is the solution


# class Employee:
#     def __init__(self, name, salary):
        # public data member
        # self.name = name
        # private member
        # self.__salary = salary

    # public instance methods
    # def show(self):
        # private members are accessible from a class
        # print("Name: ", self.name, 'Salary:', self.__salary)

# creating object of a class


# emp = Employee('Jessa', 10000)

# calling public method of the class
# emp.show()

# name mangling
class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary

# creating object of a class
emp = Employee('Jessa', 10000)

print('Name:', emp.name)
# direct access to private member using name mangling
print('Salary:', emp._Employee__salary)