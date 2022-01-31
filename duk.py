class Duck:
    def walk(self):
        print("tapak tapak")

class Horse:
    def walk(self):
        print("tapdak tapdak")

class Cat:
    def talk(self):
        print("meow meow")


def MyFunction(obj):
    if hasattr(obj,"walk"):
        obj.walk()
    if hasattr(obj,"talk"):
        obj.talk()   # Strong Typing

d=Duck()
MyFunction(d)

h=Horse()
MyFunction(h)

c=Cat()
MyFunction(c)