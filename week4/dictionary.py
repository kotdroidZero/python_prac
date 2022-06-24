# its a data type here (like map i think)
# data inside dictionaries take form of pairs of keys and values
# they are mutable
x = {"java":89,"txt":8,"png":765}

print(x)

# get value by key
print(x["java"])


# checks if Key exists in Dict
print("java" in x)


# new key value is inserted if not exists
x["html"] = 78

# value will be replaced if it exists
x["html"] = 74


print(x)

# delete any pair 
del x["html"]



print(x)

abc = {1:34,"3":334}
print(abc)


# Dictionaries are another data structure in Python. They’re similar to a list in that they can be used to organize data into collections. However, data in a dictionary isn't accessed based on its position. Data in a dictionary is organized into pairs of keys and values. You use the key to access the corresponding value. Where a list index is always a number, a dictionary key can be a different data type, like a string, integer, float, or even tuples.


#Iteration in dict

for ext in x:
    print(ext)


# items() method to get Key_Value Pair
for ext,count in x.items():
    print("There are {} file with .{} extension".format(count,ext))


# keys() method to get keys
print(x.keys())    

# values() method to get values
print(x.values())    

for value in x.values():
    print(value)

def countLetters(word):
    result ={}
    for letter  in word:
        if letter not in result:
            result[letter]=0
        result[letter]+=1

    return result        


b= countLetters("aaaadhycu dlccdksh fsdwh dadscndcgdksw")    
print(b)