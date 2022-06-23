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
















