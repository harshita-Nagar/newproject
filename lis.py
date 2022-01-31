# fruits=["apple","guava","banana","orange"]
# print(fruits)
# fruits=["apple","guava","banana","orange"]
# fruits.append("watermelon")
# print(fruits)
# print(len(fruits))
# print(type(fruits))
# fruits=list(("apple","guava","banana","orange"))
# print(fruits)
# print(fruits[2])
# print(fruits[2:4])
# print(fruits[:2])
# print(fruits[2:])
# print(fruits[-1])
# if "watermelon" in fruits:
#     print("yes")
# fruits[2]="cherry"
# print(fruits)
# fruits.insert(4,"berry")
# print(fruits)
# vegetables=["spinach","broccali","corriander"]
# fruits.extend(vegetables)
# print(fruits)
# newlist=[]
# for x in fruits:
#     if "e" in x:
#         newlist.append(x)
#         print(newlist)
# fruits=("apple","guava","banana","orange")
# y=list(fruits)
# y.append("papaya")
# fruits=tuple(y)
# print(fruits)
# fruits2=("dragonfruit","avacado")
# fruits+=fruits2
# print(fruits)

# y.remove("banana")
# fruits=tuple(y)

# for x in fruits:
#     print(fruits)

# i=0
# while i<(len(fruits)):
#     print(fruits[i])
#     i=i+1

Car=set(("waganor","suzuki","i10"))
# print("suzuki" in Car)
# Car.add("hector")
# print(Car)

Bike=set(("passion","dukati"))
# Car.update(Bike)
# print(Car)

# x=Bike.pop()
# print(Bike)

# Bike.clear()
# print(Bike)

# vehicle=Car.union(Bike)
# print(vehicle)

# Car.update(Bike)
# print(Car)

# Car.intersection_update(Bike)
# print(Car)

Car.symmetric_difference_update(Bike)
print(Car)
