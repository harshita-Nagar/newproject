# f=lambda a:a*a
# result=f(5*5)
# print(result)


# x=lambda a,b,c:a+b+c
# print(x(3,5,7))

# x = lambda a, b, c: a + b + c
# print(x(5, 6, 2))


# def my_function(n):
#     return lambda a:a*n
# mydoubler=my_function(4)
# print(mydoubler(7))


x=lambda a,b:(a+b)*4
print(x(2,3))

def my_func(n):
    return lambda a:a*n

mydoubler=my_func(2)
print(mydoubler(11))