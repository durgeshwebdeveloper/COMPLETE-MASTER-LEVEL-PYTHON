# Arrays are used to store multiple values in one single variables.
cars = [ "ford", "valvo", "bmw"]
print(cars)   # Output:['ford', 'valvo', 'bmw']

# Accessing the elements of an arrays
cars = [ "ford", "valvo", "bmw"]
x = cars[1]
print(x)     # Output:valvo

# Modifying the values of arrays
cars = [ "ford", "valvo", "bmw"]
cars[0]  = " Toyota"
print(cars)      # Output:valvo

# Length of an Array
cars = [ "ford", "valvo", "bmw"]
x = len(cars)
print(x)     # Output: 3

# Looping an array elements
cars = ["ford", "valvo", "bmw"]
for i in  cars:
    print(cars)    # Output: ['ford', 'valvo', 'bmw']
                            #['ford', 'valvo', 'bmw']
                            #['ford', 'valvo', 'bmw']

# Adding arrays elements
cars = ["ford", "valvo", "bmw"]
cars.append("Honda")
print(cars)     # Output:['ford', 'valvo', 'bmw', 'Honda']

# Removing an array elements 
cars = ["ford", "valvo", "bmw"]
cars.pop(1)
print(cars)      # Output:['ford', 'bmw']

# Another remove function for removing
cars = ["ford", "valvo", "bmw"]
cars.remove("valvo")
print(cars)    # Output:['ford', 'bmw']

# All types of arrays methods
# append()
# clear()
# copy()
# count()
# extend()
# index()
# pop()
# remove()