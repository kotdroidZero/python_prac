

# list is mutable


x = [1,2,3,56,423,123,455,67,64764,432,424]
print(x)
print(type(x))

print(len(x))

print(2 in x)
print(x[1])
#print(x[35]) # indexError out of range

print(x[:2])
print(x[:2])
print(x[4:])


fruits = ["apple","Banana"]

fruits.append("Kiwi")
print(fruits)

fruits.insert(0,"Oranges")
print(fruits)

fruits.remove("Oranges")
print(fruits)

#fruits.remove("Oranges")

popped = fruits.pop(2)
print(popped)
print(fruits)
fruits[0]="Mango"

print(fruits)


