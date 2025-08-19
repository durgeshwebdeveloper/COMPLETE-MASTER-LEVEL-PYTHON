class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)

x = person("durgesh", "durex")
x.printname()     #Ouput:durgesh durex

#Creating a Child Class
class student(person):
    pass
# Testing the student class
class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
class student(person):
    pass
x = student("durgesh", "durexnew")
x.printname()     #Ouput:durgesh durexnew

# Adding __init__() function

class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
class student(person):
    def __init__(self, fname, lname):
        person.__init__(self, fname, lname)
x = student("durgesh", "durex")
x.printname()     #Output: durgesh durex

#Using the super() function
class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
class student(person):
    def __init__(self, fname, lname):
        super().__init__(fname,lname)
x = student("durgesh", "durexnew1")
x.printname()     #Output: durgesh durexnew1

# How to add the properties.
class person:
    def __init__(self, fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
class student(person):
    def __init__(self, fname, lname):
        super().__init__(fname,lname)
        self.graduationyear = 2022
x = student("durgesh", "durex")
print(x.graduationyear)   #Output:2022

# You can pass the object property in student directly.
class person:
    def __init__(self,fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
class student(person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
x = student("durgesh","durex", 2021)
print(x.graduationyear)    #2021