class Student:
    def __init__(self,name):
        self.name=name
        print("Inside Constructor")

        def show(self):
            print("Hello, my name is ", self.name)


    def __del__(self):
        print("Object destructed")


s1=Student("Leena")
s1.show()

del s1