# /# n=int(input("enter a number:"))
# #
# # x=0
# # y=1
# # z=0
# # while n<=z:
# #     x=y
# #     y=z
# #     z=x+y
#
# nterms = int(input("How many terms? "))
#
# n1, n2 = 0, 1
# count = 0
# if nterms <= 0:
#    print("Please enter a positive integer")
# elif nterms == 1:
#    print("Fibonacci sequence upto", nterms, ":")
#    print(n1)
# else:
#    print("Fibonacci sequence:")
#    while count < nterms:
#        print(n1)
#        nth = n1 + n2
#        n1 = n2
#        n2 = nth
#        count += 1


def fibrecur(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibrecur(n-1)+fibrecur(n-2)


if __name__=="__main__":
    num=int(input("Enter the number:"))
    print(f"This is the result of recursion:  {fibrecur(num)}")

# import time
# def fiboiter(n):
#     prevnum=0
#     currentnum=1
#     for i in range(1,n):
#        preprevnum=prevnum
#        prevnum=currentnum
#        currentnum=preprevnum+prevnum
#     return currentnum
#
# if __name__=="__main__":
#     num=int(input("Enter the number:"))
#     init=time.time()
#     print(f"This is the result of recursion:  {fiboiter(num)}")
#     print(f"It took {time.time()-init} seconds")


