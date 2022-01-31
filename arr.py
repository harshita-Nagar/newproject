# import array as ar
# a=ar.array('i', [1,2,3,4,5,6])
# print(a)
# len(a)

# x=a[0]
# print(x)

# a[2]=8
# print(a)

# a.append(10)
# print(a)

# a.remove(4)
# print(a)

#print(sum(a))
# print(sum(a, -1))

# def reverseword(s):
#     return s[:: -1]
#     reverseword(s)
#
#
# prac = reverseword("Hello World")
# print("This is the reverse string:",prac)  # reversing the string

from array import *


def sorting_array():
 arr=array('i',[45,78,56,23,90,12])
for i in range (len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]

print(arr)





