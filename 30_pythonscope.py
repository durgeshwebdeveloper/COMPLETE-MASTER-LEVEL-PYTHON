# What is Scope? - a variable is only available from inside the region it is created and this called scope. 
 
# What is Local Scope?
def myfunc():
    x = 300
    print(x)
myfunc()   #Output: 300

# Function inside function
def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc()    # Output: 300

# What is Global Scope?
x = 300
def myfunc():
    print(x)
myfunc()    # Output: 300

# Naming variable - python will treat the 2 variable as a separate variables.
x = 300
def durgesh():
    x = 200
    print(x)
durgesh()    #Output:200
print(x)   # Output:300

# Global Variable - if you need to create a global variable locally then you should use global keyword.
def durgesh():
    global x 
    x = 300
durgesh()
print(x)   #Output: 300

# You can also use the global keyword if you want to make a change to a global variable inside the function.
x = 500
def durgesh():
    global x 
    x = 200
durgesh()
print(x)  # Output: 200