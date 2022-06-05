# defining function
#We start a function definition with the def keyword, followed by the name we want to give our function. After the name, we have the parameters, also called arguments, for the function enclosed in parentheses. A function can have no parameters, or it can have multiple parameters. Parameters allow us to call a function and pass it data, with the data being available inside the function as variables with the same name as the parameters. Lastly, we put a colon at the end of the line.
#After the colon, the function body starts. It’s important to note that in Python the function body is delimited by indentation. This means that all code indented to the right following a function definition is part of the function body. The first line that’s no longer indented is the boundary of the function body. It’s up to you how many spaces you use when indenting - - just make sure to be consistent. So if you choose to indent with four spaces, you need to use four spaces everywhere in your code.
import re


def greeting(name,department):
      print("Welcome "+ name)
      print("You are from "+ department)

def function2():
    print("I am function 2")
    


function2()
greeting("Pushkar Srivastava","Mobile Application Development")

# we cannot simply add any data type in string, we need to coonver that in string using str() function look below
#print("The number is"+9) 
print("The number is "+str(9))

# function returning value
def calculateArea(base, height):
    return (base*height)/2

base =38
height =4
# area = (base*height)/2
area = calculateArea(base,height)
print("Triangle's area is :"+str(area))

# just wooow , in python function can return multiple values
# take a look below
def calculatePowers(num):
     powerOne = num**num
     powerTwo = powerOne**num
     powerThree = powerTwo**num
     return powerOne,powerTwo,powerThree

num1,num2,num3= calculatePowers(2)
print(num1, num2, num3)    


# returning nothing 
# None: A special data type in Python used to indicate that the things are
# empty or they returned nothing

value = function2()
print(value)

name = "Pushkar Srivastava"
print(len(name))

