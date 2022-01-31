# def inc(x):
#     return x+1
#
#
# def operate(func,x):
#     result=func(x)
#
#     return result
#
#
# # print(inc(6))
# # or
# print(operate(inc,6))
#
#
# def print_msg(message):
#     greeting="Hello"
#
#
#     def printer():
#         print(greeting, message)
#
#     printer()
#
#
# print_msg("Python is awesome")
#
#
# # Closure function (below)
# def print_msg(message):
#     greeting="Hello"
#
#
#     def printer():
#         print(greeting, message)
#
#     return printer
#
#
# func=print_msg("Python is awesome")
# func()
#
#
# def printer():   # without @ decorator
#     print("Hello World!")
#
#
# def dispaly_info(func):
#
#     def inner():
#         print("Executing",func.__name__, "function")
#         func()
#         print("finished execution")
#
#     return inner()
#
#
# decorated_func=dispaly_info(printer)
# decorated_func()
#
#
# # with decorator
# # example 1
#
# def dispaly_info(func):
#
#     def inner():
#         print("Executing",func.__name__, "function")
#         func()
#         print("finished execution")
#
#     return inner()
#
#
# @dispaly_info
# def printer():
#     print("Hello World!")
#
#
# printer()
#
#
# # Example2
#
# def smart_divide(func):
#     def inner(a,b):
#         print("Dividing", a, "by", b)
#         if b==0:
#             print("can't be divided")
#             return
#         return func(a,b)
#     return inner()
#
#
# @ smart_divide
# def divide(a,b):
#     return a/b
#
# value1=(9,2)
# print(value1)
#
# value2=(8,0)
# print(value2)


def outer():
    x=3
    def inner():
        y=4
        result=x+y
        return result
    # return inner   without (), it will return the memory location
    return inner()  # return the + of x and y

a=outer()
del(outer)
print(a)


