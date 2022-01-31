def pypart(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end="")
        print("/r")


n=5
pypart(n)



row=5
for i in range(row):
    for j in range(i):
        print(i,end="")
    print(" ")