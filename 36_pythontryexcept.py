'''try - block let you test a block of code for error. 
except - block lets you handle the error. 
else - block lets you execute the code when there is no error. 
finally - block lets you execute the code regardless of the result of try and except block .'''

# Example of try block 
try:
    print(x)
except:
    print("an error occured ")  #Output: an error occured 

# If try and except is not given 
print(x)

# Many exceptions - you can even define many exceptions block. 
try:
    print(x)
except NameError:
    print("Variable of x is not defined")
except:
    print("Something else went wrong")         #Output: Variable of x is not defined

# Else - you can use the else keyword to define a block of code to be executed if no error. 
try: 
    print("Hello")   #Output: Hello
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")    #Output:  Nothing went wrong

# Finally  - 
try:
    print(x)
except:
    print("Something went wrong")    #Output:Something went wrong
finally:
    print("The 'try' except is finished")    #Output: The 'try' except is finished

# Example :
try:
    f = open("demofile.txt")
    try:
        f.write("durgesh gupta")
    except:
        print("Something went wrong when writitng to the file")    
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")        #Output:   Something went wrong when writitng to the file

# Raise an Exception  = -1 
x = "durgesh"
if not type(x) is int:
    raise TypeError("only integer are allowed")

