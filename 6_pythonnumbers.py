x = 1
y = 2.5
z = 1j
print(type(x))    #Ouput:<class 'int'>
print(type(y))    #Ouput:<class 'float'>
print(type(z))    #Ouput:<class 'complex'>

# int numeric type
x = 1
y = 78676786786
z = -8787
print(type(x))    #Ouput:<class 'int'>
print(type(y))    #Ouput:<class 'int'>
print(type(z))    #Ouput:<class 'int'>

# Float or Floating point number Data Type
x = 1.10
y = 1.0
z = -25.47
print(type(x))    #Ouput:<class 'float'>
print(type(y))    #Ouput:<class 'float'>
print(type(z))    #Ouput:<class 'float'>

#Float can also be scientific numbers with an "e" = power of 10.

x = 35e3
y = 12E4
z = -87.7e155
print(type(x))    #Ouput:<class 'float'>
print(type(y))    #Ouput:<class 'float'>
print(type(z))    #Ouput:<class 'float'>

#Complex numbers are written with a "j" as the imaginary part.
x = 3+5j
y = 7j
z = -8j
print(type(x))    #Ouput:<class 'complex'>
print(type(y))    #Ouput:<class 'complex'>
print(type(z))    #Ouput:<class 'complex'>

#Type Conversion

x = 1
y = 2.8
z = 1j

#Convert form int to float
a = float(x)
print(a)    #Ouput:1.0

#Convert from float to int
b = int(y)
print(b)   #Ouput:2

#Convert from int to complex

c = complex(x)
print(c)   #Ouput:(1+0j)

print(type(a))       #Ouput:<class 'float'>
print(type(b))       #Ouput:<class 'int'>
print(type(c))       #Ouput:<class 'complex'>

#Random Number
import random
print(random.randrange(1,10))     #Ouput:Random number between (1,10)
