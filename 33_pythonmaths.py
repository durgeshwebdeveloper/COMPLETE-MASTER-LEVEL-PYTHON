# Python has a extensive maths built-in function.

# Buil-in  Maths function 
# Min() and Max() - maths function 
x = min(5, 20 , 25 )
y = max(5, 10 , 20 , 25 )
print(x)   #Output: 5
print(y)   #Output: 25

# abs() - this function returns absolute positive value.
x  = abs(-493.34)
print(x)      #Output: 493.34

# pow(x,y) - this function returns the value of x to the power of y. 
x = pow( 4 , 3 )   # Same as 4*4*4
print(x)       #Output: 64

# We can also import maths module externally
import math 
x = math.sqrt(81)
print(x)   #Output: 9

# math.ceil() and math.floor()
x = math.ceil(1.4)   # nearest to upward 
y = math.floor(1.4)  # nearest to downward
print(x)    #Output: 2
print(y)    #Output: 1

# math.pi 
import math 
x = math.pi 
print(x)    #Output:   3.141592653589793