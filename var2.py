# c = 1  # global variable
#
#
# def add():
#     c = c + 2  # increment c by 2
#     print(c)
# UnboundLocalError: local variable 'c' referenced before assignment


# add()
# c=1 # global variable
# def add():
#     global c
#     c=c+2
#     print("inside add():",c)
#     add()
#     print("in main:",c)

# c = 0  # global variable
#
# def add():
#     global c
#     c = c + 2  # increment by 2
#     print("Inside add():", c)
#
#     add()
#     print("In main:", c)
x="awesome"
def myfun():
    x="fantastic" #local
    print("python is", + x)
    myfun()
    print("python is ", + x)






