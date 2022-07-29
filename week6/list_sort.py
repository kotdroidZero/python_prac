import numbers
from unicodedata import name


numbers = [3,1,45,23,3]
numbers.sort()
print(numbers)

names=['Rahul','Raj','Abhay','Aanchal']
print(names)
print(sorted(names))
print(names)


print(sorted(names,key=len))