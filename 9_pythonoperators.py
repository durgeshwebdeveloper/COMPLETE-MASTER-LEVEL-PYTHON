# Arithmetic Operators
# Assignment Operators
# Comparison Operators
# Logical Operators
# Identity Operators
# Membership Operators
# Bitwise Operators

# Arithmetic Operators

x = 10
y = 5
print(x + y)   #Output:15

x = 10
y = 5
print(x - y)   #Output:5

x = 10
y = 5
print(x * y)    #Output:50

x = 10
y = 5
print(x / y)   #Output:2.0

x = 10
y = 5
print(x % y)    #Output:0

x = 10
y = 5
print(x ** y)   #Output:100000

# Assignment Operators

# x = 5
# x = x + 5   same as x += 5
# x = x - 5   same as x -= 5
# x = x * 5   same as x *= 5
# x = x / 5   same as x /= 5
# x = x % 5   same as x %= 5
# x = x ** 5  same as x **= 5

x = 5 
x **= 3 
print(x)  #Output:125


# Comparison Operators 

x = 5
y = 3
print( x == y)  #Output: False

x = 5
y = 3
print(x != y)   #Output:True

x = 5 
y = 3
print(x > y)   #Output: True

x = 5
y = 3
print(x < y)  #Output:False
 
x = 5
y = 3
print(x >= y)   #Output: True

x = 5
y = 3
print(x <= y)   #Output: False

# Logical Operators

x = 5
print(x > 3 and  x < 10)  #Output: True

x = 5
print(x > 3 or x < 4)   #Output:True

x = 5
print(not(x > 3 and x < 10))   #Output:False

# Identity Operators
x  = [ " Durgesh", "Durex"]
y =  [ " Durgesh", "Durex"]
z = x 
print(x is z)   # returns true because z is the same object as x.
#Output:True

print(x is y)   # returns false because x is not the same object as y even if they have the same content.
#Output:False

print( x == y)  # to demonstrate the difference between "is" and " == " , this comparison returns  True because x is equal to y.
#Output:True


# Membership Operator
x = ["apple", "banana", "laddu", "peda"]
print("banana" in x)   #Output: True

x = ["apple", "banana", "laddu", "peda"]
print("bsdfed" in x)     #Output: False

x = ["apple", "banana", "laddu", "peda"]
print("Pineapple" not in x)   #Output: True

x = ["apple","banana", "laddu", "peda"]
print("banana" not in x)     #Output: False