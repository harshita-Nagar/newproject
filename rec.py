 b# import sys
# sys.setrecursionlimit(100)
#
# print(sys.getrecursionlimit())
# i=0
#
# def greet():
#     global i
#     i+=1
#     print("hello" , i)
#     greet()
#
# greet()

# def fact(n):
#    if n==1:
#        return 1
#        return n* fact(n+1)
#
# n=5
# result=fact(5)
# print(result)

def  factorial(n):
    return 1 if  (n==1 or n==0) else n * factorial(n-1);

num=5
print("factorial of",  num, "is" ,factorial(num) )

# return 1 if (n == 1 or n == 0) else n * factorial(n - 1)
