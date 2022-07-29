class Apple:
    def __init__(self,color,flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self)    :
        return "This is apple of {} color and its flavor is {}".format(self.color, self.flavor)

apple1 =Apple("Red","Sweet")        

print(apple1.color)
print(apple1.flavor)

print(apple1)

# Special Methods
# Instead of creating classes with empty or default values, we can set these values when we create the instance. This ensures that we don't miss an important value and avoids a lot of unnecessary lines of code. To do this, we use a special method called a constructor. Below is an example of an Apple class with a constructor method defined.
# class Apple:
# ...     def __init__(self, color, flavor):
# ...         self.color = color
# ...         self.flavor = flavor


# When you call the name of a class,  the constructor of that class is called.
#  This constructor method is always named __init__. 
# You might remember that special methods start and end with two underscore characters. 
# In our example above, the constructor method takes the self variable, which represents the 
# instance, as well as color and flavor parameters. 
# These parameters are then used by the constructor method to set the values for the current instance. 
# So we can now create a new instance of the Apple class and set the color and flavor values all in go:



# In addition to the __init__ constructor special method, there is also the __str__ special method. This method allows us to define how an instance of an object will be printed when it’s passed to the print() function. If an object doesn’t have this special method defined, it will wind up using the default representation, which will print the position of the object in memory. Not super useful. Here is our Apple class, with the __str__ method added:

help(Apple)



class Person:
  def __init__(self, name):
    self.name = name
  def greeting(self):
    """Outputs a message with name of the person."""
    print("Hello! My name is {name}.".format(name=self.name)) 

help(Person)


# Documenting with Docstrings
# The Python help function can be super helpful for easily pulling up documentation for classes and methods. We can call the help function on one of our classes, which will return some basic info about the methods defined in our class:

# We can add documentation to our own classes, methods, and functions using docstrings. A docstring is a short text explanation of what something does. You can add a docstring to a method, function, or class by first defining it, then adding a description inside triple quotes. Let's take the example of this function:

