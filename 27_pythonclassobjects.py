# Create a Class
class myclass:
    x = 5
print(myclass)    #Ouput:<class '__main__.myclass'>

# Create object
class myclass:
    x = 5
p1 = myclass()
print(p1.x)     # Output:5

# The_init_() function
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = person("Durgesh",23)
print(p1.name)  #Output: Durgesh
print(p1.age)   #Ouput:23

# Object Method
class person:
    def __init__(self, name, age):
        self.name  = name
        self.age = age
    def myfunc(self):
        print("Hello everyone my name is " + self.name)
p1 = person("Durgesh" , 23)
p1.myfunc()   #Ouput:Hello everyone my name is Durgesh

# The self parameter {self ki jagah kuchh bhii likh sakte hai bhai log samajh lo kalle se}
class person:
    def __init__(durgeshobject, name, age):
        durgeshobject.name = name
        durgeshobject.age = age
    def myfunc(abc):
        print("Hello everyone my name is " + abc.name)
p1 = person("durgesh ",36)
p1.myfunc()     #Ouput:Hello everyone my name is Durgesh

# How to modify object properties.
class person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def myfunc(self):
        print("hello everyone my name is " + self.name)
p1 = person("durgesh", 23)
p1.age = 40
print(p1.age)    #Ouput:40

# Delete Object Properties.
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello everyone my name is " +  self.age)
p1 = person("durgesh", 23)
del p1.age
print(p1.name)     #Ouput:durgesh

# How to delete object
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello everyone my name is " + self.name)
p1 = person("durgesh", 23)
del p1

#The pass statement
class person:
    pass