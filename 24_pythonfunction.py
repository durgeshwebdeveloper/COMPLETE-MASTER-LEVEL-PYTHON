print("hello this is a durgesh durex")   # Output:hello this is a durgesh durex

# Creating and calling a function
def my_function():
    print("Hello this is new durgesh durex.")
my_function()   #Output:Hello this is new durgesh durex.

# Definition of Arguments(args)-  arguments are specified after the function name and inside the parenthesis.
def my_function(fname):
    print(fname + "durex")
my_function("durgesh")      # Output:durgeshdurex
my_function("sanjay")       # Output:sanjaydurex
my_function("pratima")      # Output:pratimadurex

# Number of arguments - 2 args
def my_function(fname , lname):
    print(fname + " " + lname)
my_function("durgesh", "durex")     # Output:durgesh durex

# Arbitrary Arguments - *args
def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function("chintu", "mintu", "pinku")      # Output:The youngest child is pinku

# Keyword Arguments key = value
def my_function(child1,  child2, child3):
    print("The youngest child is " + child3)
my_function(child3 = "chintu", child1 = "mintu", child2 = "pintu")    #Output:The youngest child is chintu

# Arbitrary keyword argumetns **kwargs
def my_function(**kids):
    print("His last name is " + kids["lname"])
my_function(fname = "durgsh", lname = "durex")    #Output:His last name is durex

# Default Parameter value
def my_funciton(country = "India"):
    print("I am from " + country)
my_funciton("Canada")   #Output:I am from Canada
my_funciton("UK")       #Output:I am from UK
my_funciton()           #Output:I am from India
my_funciton("Australia")     #Output:I am from Australia

# Passing a list as an argument 
def my_function(fruits):
    for i in fruits:
        print(i)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)          #Output:  apple  banana   cherry

# Return values- To let a function return a value then you use return statement
def my_function(x):
    return 5 * x
print(my_function(3))          #Output: 15
print(my_function(5))          #Output: 25
print(my_function(9))          #Output: 27

# The pass Statement 
def my_function():
    pass
