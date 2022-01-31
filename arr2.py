# merging two sorted array
# def merge_two_sorted_list(a,b):
#     sorted_list=[]
#     len_a=len(a)
#     len_b=len(b)
#     i=j=0
#
#     while i<len_a and j< len_b:
#         if a[i]<b[j]:
#             sorted_list.append(a[i])
#             i+=1
#         else:
#             sorted_list.append(b[j])
#             j+=1
#     while i< len_a:
#         sorted_list.append(a[i])
#         i+=1
#     while j<len_b:
#         sorted_list.append(b[j])
#         j+=1
#     return sorted_list
#
#
#
# if __name__=='__main__':
#     a=[5,8,12,56]
#     b=[7,9,45,51]
#
#     print(merge_two_sorted_list(a,b))


# sorting one array

# arr=[9,4,2,6,7]
# temp=0
#
# for i in range(0,len(arr)):
#     for j in range(i+1,len(arr)):
#         if (arr[i]>arr[j]):
#             temp=arr[i];
#             arr[i]=arr[j];
#             temp=arr[j];
#
# print();
#
# for i in range(0,len(arr)):
#     print(arr[i],end="")

arr = [5, 2, 8, 7, 1];
temp = 0;

# Displaying elements of original array
print("Elements of original array: ");
for i in range(0, len(arr)):
    print(arr[i], end=" ");

# Sort the array in ascending order
for i in range(0, len(arr)):
    for j in range(i + 1, len(arr)):
        if (arr[i] > arr[j]):
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;

print();

# Displaying elements of the array after sorting

print("Elements of array sorted in ascending order: ");
for i in range(0, len(arr)):
    print(arr[i], end=" ");





