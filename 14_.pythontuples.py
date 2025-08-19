x = ( "durgesh", "banana", "orange")
print(x)  #Output:('durgesh', 'banana', 'orange')

# Tuple length
x = ("durgesh", "banana", "orange")
print(len(x))   #Output: 3

# Create tuple with one item
x = ("durgesh",)
print(type(x))   #Output:<class 'tuple'>

# Not a tuple
x = ("durgesh")
print(type(x))   #Output : <class 'str'>

# Tuple items _ data type(String, int, boolean)
x = ("durgesh", "banana","orange")
y = (1,2,3,4,5)
z = (True, False, True)
print(x)   #Output:('durgesh', 'banana', 'orange')
print(y)   #Output:(1, 2, 3, 4, 5)
print(z)    #Output:(True, False, True)

# Tuple can also contain different data type
x = ("durgesh", 35, True, 50, "male")
print(x)       #Output:('durgesh', 35, True, 50, 'male')

# The tuple() constructor
durgesh = tuple(("apple", "banana", "cherry"))
print(type(durgesh))    #Output:<class 'tuple'>

# Access tuple items
x = ("durgesh", "banana", "orange")
print(x[1])    #Output: banana

# Access tuple items through negatve indexes
x =  ("durgesh", "banana", "orange")
print(x[-1])  #Orange: orange

#Access tuple items through range of indexes
x = ("durgesh", "banana", "orange", "cherry", "papaya", "kiwi", "mango")
print(x[2:5])   #Output:('orange', 'cherry', 'papaya')

# Access tuple items through range of indexes but some index not inlcuded.
x = ("durgesh","banana", " orange", "cherry", "papaya","kiwi", "mango")
print(x[2:])     #Output:(' orange', 'cherry', 'papaya', 'kiwi', 'mango')

# Access tuple itemsthrough negativve range of indexes.
x = ("durgesh", "banana", "orange", "cherry", "papaya", "kiwi", "mango")
print(x[-4:-1])       #Output:('cherry', 'papaya', 'kiwi')

# Check if the item exists
x = ("durgesh","banana", "orange", "cherry", " papaya", "kiwi", "mango", "melon", "nuts", "durex")
if "orange" in x :
    print("Yes, 'orange is in x")    #Output:Yes, 'orange is in x

    # ( Very Important) Changing of Tuple Value

x = ("durgesh", "banana", "orange", "cherry", "papaya", "kiwi", "mango", "melon", "nuts", "durex")
print(type(x))     #Output:<class 'tuple'>
y= list(x)
print(type(y))     #Output:<class 'list'>
y[1] = "Python"
x = tuple(y)
print(x)           #Output: ('durgesh', 'Python', 'orange', 'cherry', 'papaya', 'kiwi', 'mango', 'melon', 'nuts', 'durex')
print(type(x))     #Output: <class 'tuple'>

# Add items in tuple (Very Important)
x = ("durgesh", "banana", "orange", "cherry", "papaya", "kiwi", "mango", "melon", "melon", "nuts", "durex")
print(type(x))     #Output:<class 'tuple'>
y = list(x)
print(type(y))      #Output:<class 'list'>
y.append("lastvalue")
x = tuple(y)
print(x)      #Output:('durgesh', 'banana', 'orange', 'cherry', 'papaya', 'kiwi', 'mango', 'melon', 'melon', 'nuts', 'durex', 'lastvalue')

# Adding tuple to a tuple
x = ("apple", "orange", "banana")
y = ("cherry", )
x += y
print(x)    #Output:('apple', 'orange', 'banana', 'cherry')

# Removing items to a tuple
x = ("durgesh", "banana", "orange", "cherry", "papaya", "kiwi", "mango", "melon", "nuts", "durex")
print(type(x))    #Output:<class 'tuple'>
y = list(x)
print(type(y))    #Output:<class 'list'>
y.remove("durex")
x = tuple(y)
print(x)    #Output:('durgesh', 'banana', 'orange', 'cherry', 'papaya', 'kiwi', 'mango', 'melon', 'nuts')

# How to delete tuple
x = ("durgesh", "banana", "orange", "cherry", "papaya", "kiwi", "mango", "melon", "nuts", "durex")
del x

# Packing a tuple (when we assign a values to tuple)
x = ("durgesh", "durex", "banana")

#Unpacking the tuple (when we extract the value from the tuple)

x = ("durgesh", "durex", "banana")
(green, yellow, red) = x
print(green)    #Output: durgesh
print(yellow)   #Output:durex
print(red)      #Output: banana

# How to assign for the rest of the values in tuple
x = ("durgesh", "durex", "banana", "cherry", "apple")
(green, yellow, *red) = x
print(green)     #Output:durgesh
print(yellow)    #Output:durex
print(red)       #Output:['banana', 'cherry', 'apple']
