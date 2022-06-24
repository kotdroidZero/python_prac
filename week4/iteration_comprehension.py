


winners = ["Sarthak","Prince","Deepak"]

for index, person in enumerate(winners):
    print("{} -> {}".format(index+1,person))



#Iterating Over Lists Using Enumerate
#When we covered for loops, we showed the example of iterating over a list. This lets you iterate over each element in the list, exposing the element to the for loop as a variable. But what if you want to access the elements in a list, along with the index of the element in question? You can do this using the enumerate() function. The enumerate() function takes a list as a parameter and returns a tuple for each element in the list. The first value of the tuple is the index and the second value is the element itself.
def getFormattedNameAndEmail(nameList):
    for index,name in enumerate(nameList):
        print("{}<{}>".format(name.lower(),name.lower()+"@infostride.com"))


def fullEmails(people):
    result=[]
    for name , email in people:
        result.append("{}<{}>".format(name,email))
    return result    

peopleTupple   = [("Pushkar","pushkar@yopmail.com"),("Mohit","mohit@yopmail.com")]
print(fullEmails(peopleTupple))

getFormattedNameAndEmail(winners)


# we can have operation or looping or condition inside loop also
# for example
a = [ x for x in range(1,18) if(x%2==0)]
print(a)




# Basic operation for printing multiple of 5
multiples=[]
for x in range(1,11):
    multiples.append(x*5)
print(multiples)    


# Now See the same with List Comprenehension
# List Comprehensions creates new list based on sequesnces and ranges
multiples1 = [x*7 for x in range(1,11)]
print(multiples1)

#List-specific operations and methods
#list[i] = x Replaces the element at index i with x

#list.append(x) Inserts x at the end of the list

#list.insert(i, x) Inserts x at index i

#list.pop(i) Returns the element a index i, also removing it from the list. If i is omitted, the last element is returned and removed.

#list.remove(x) Removes the first occurrence of x in the list

#list.sort() Sorts the items in the list

#list.reverse() Reverses the order of items of the list

#list.clear() Removes all the items of the list

#list.copy() Creates a copy of the list

#list.extend(other_list) Appends all the elements of other_list at the end of list