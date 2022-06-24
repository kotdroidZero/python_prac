#prints all methods 
# print(dir(""))


# shows how to use a particular function of any class
# print(help(int))

class Animal:
    name="Janwar"
    def speak(self):
        print("Hello I'm Animal , my name is{}".format(self.name))

dog = Animal()
dog.name = "Shera T"
dog.speak()

