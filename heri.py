# class Person:
#      def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname
#      def printname(self):
#          print(self.firstname,self.lastname)
#
# x=Person("john","sinah")
# x.printname()

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self,fname,lname):
    super. __init__(fname,lname)
    self.graduationyear=2019

x = Person("John", "Doe")
print(x.graduationyear)