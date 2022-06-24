# string "" or in ''
# "abc" *3 => abcabcabc
# len("abc") => 3 (length of characters)
# String is immutable

text= "Pythons is scriptin  fhfj wff"

print(text[0])  # prints P
print(text[3])   # prints h

print(text[-1])   # prints character from end of the string prints f
print(text[1:4])

fruit = "Mangosteen"


# Processing substring
a=fruit[1:4] #'ang'
print(a)
b= fruit[:5]  #'Mango'
print(b)
c= fruit[5:]  #'steen'
print(c)




# Strings are immutable in Python

#Get Index of any Substring
print(fruit.index("e"))

# contains to check substring in a String, look the same in Python
d= "b" in fruit
print(d)


# few more methods
answer = "YES"
print(answer.lower())
answer = "yes"
print(answer.upper())

answer =  "    yes    "
print(answer)
# kind of trim() which remove whitespaces from start and end
print(answer.strip())
print(answer.lstrip())
print(answer.rstrip())
print(answer.count("e"))   # how many time substrings occured
print(answer.endswith("p"))
print("123456".isnumeric())
print(int("12345"))   #parsing of string to int

# join() for concatination 
joinEx= " ".join(["This","is","Majak"])
print(joinEx)

print(joinEx.split(" "))

#formatting a string
name1 = "Pushkar"
age1 = len(name1)*4
print("Hello {}, your age is {}".format(name1,age1))
#or
print("Hello {name}, your age is {age}".format(name=name1, age=age1))

# the formatting expression {:.2f} means that you’d format this as a float number, with two digits after the decimal dot
#  the expression {:>3.2f} would align the text three spaces to the right, as well as specify a float number with two decimal places.


#String operations
# 1. len(string) Returns the length of the string
# 2. for character in string Iterates over each character in the string
# 3. if substring in string Checks whether the substring is part of the string
# 4. string[i] Accesses the character at index i of the string, starting at zero
# 5. string[i:j] Accesses the substring starting at index i, ending at index j-1. If i is omitted, it's 0 by default. If j is omitted, it's len(string) by default.


#String methods
# 1. string.lower() / string.upper() Returns a copy of the string with all lower / upper case characters
# 2. string.lstrip() / string.rstrip() / string.strip() Returns a copy of the string without left / right / left or right whitespace
# 3. string.count(substring) Returns the number of times substring is present in the string
# 4. string.isnumeric() Returns True if there are only numeric characters in the string. If not, returns False.
# 5. string.isalpha() Returns True if there are only alphabetic characters in the string. If not, returns False.
# 6.string.split() / string.split(delimiter) Returns a list of substrings that were separated by whitespace / delimiter
# 7. string.replace(old, new) Returns a new string where all occurrences of old have been replaced by new.
# 8. delimiter.join(list of strings) Returns a new string with all the strings joined by the delimiter






# The permissions of a file in a Linux system are split into three sets of three permissions: read, write, and execute for the owner, group, and others. Each of the three values can be expressed as an octal number summing each permission, with 4 corresponding to read, 2 to write, and 1 to execute. Or it can be written with a string using the letters r, w, and x or - when the permission is not granted.
#  For example: 
#  640 is read/write for the owner, read for the group, and no permissions for the others; converted to a string, it would be: "rw-r-----"
#  755 is read/write/execute for the owner, and read/execute for group and others; converted to a string, it would be: "rwxr-xr-x"
#  Fill in the blanks to make the code convert a permission in octal format into a string format.
 
def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for num in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if num >= value:
                result += letter
                num -= value
            else:
                result+="-"
    return result
    
print(octal_to_string("755")) # Should be rwxr-xr-x
print(octal_to_string("644")) # Should be rw-r--r--
print(octal_to_string("750")) # Should be rwxr-x---
print(octal_to_string("600")) # Should be rw-------








