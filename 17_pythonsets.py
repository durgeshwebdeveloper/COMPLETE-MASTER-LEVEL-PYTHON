# What are sets => (Unordered, Unchangeable, unindexed)
x = {"a", "b", "c", "a"}
print(x)    #Output:{'a', 'b', 'c'}

# Duplicate not Allowed
x = {"a", "b", "c", "a"}
print(x)    #Output:{'a', 'c', 'b'}

# Get the length of the set
durgesh = {"apple", "banana", "cherry"}
print(len(durgesh))

# How to check the Data types of Set
set1  = {"a","b", "c"}
set2 = {1,5,9,7,6}
set3 = {True, False, True}
print(type(set1))     #Output:<class 'set'>
print(type(set2))     #Output:<class 'set'>
print(type(set3))     #Output:<class 'set'>

# The set() with string , integer and Boolean means all data types
set1 = {"abc", 35, True, 40, "male"}
print(set1)    #Output:{True, 35, 'abc', 'male', 40}

# The Set() Constructor
thisset = set(("a", "b", "c"))
print(thisset)   #Output:{'c', 'a', 'b'}

# How to Access Items in set through looping 
durgesh = {"a", "b", "c"}
for i in durgesh:
    print(i)   #Output: a
                      # b
                      # c

# Check if banana is present or not
durgesh = {"apple", "banana", "mango"}
print("banana" in durgesh)    #Ouput: True

# Adding set items
durgesh = {"apple", "banana", "mango"}
durgesh.add("orange")
print(durgesh)    #Output: {'apple', 'mango', 'banana', 'orange'}

# How to add items from another set into the current set
durgesh = {"apple", "banana", "mango"}
pratima = {"pineapple", "mango", "papaya"}
durgesh.update(pratima)
print(durgesh)      #Output: {'mango', 'banana', 'papaya', 'apple', 'pineapple'}

# How to remove set items
durgesh = {"red", "blue", "green"}
durgesh.remove("blue")
print(durgesh)    #Output:{'red', 'green'}

# How to use discard() for removing the items in set
durgesh = {"red", "blue", "green"}
durgesh.discard("red")
print(durgesh)      #Ouput:{'blue', 'green'}

# Remove the last item by using the pop() method will raise the error or you will get the wrong outputs.
durgesh = {"black", "pink", "orange"}
x = durgesh.pop()
print(x)    #Ouput: black
print(durgesh)    #Output:  {'orange', 'pink'}

# The clear() method isused for empty the set
durgesh = {"rd", "blue", "green"}
durgesh.clear()
print(durgesh)

# The Del keyword is used to delete the set completly.
durgesh = {"Red", "blue", "green"}
del durgesh      #Output: set()

# How to loop through the set
durgesh = {"watermelon", "orange", "black"}
for i in durgesh:
    print(i)    #Output: orange
                        # watermelon
                        # black

# How to join the two sets by union()
set1 = {"red", "blue", "green"}
set2 = {1,2,3}
set3 = set1.union(set2)
print(set3)    #Output: {1, 2, 3, 'blue', 'green', 'red'}

# How to join the two sets by updates()
set1 = {"red", "blue", "green"}
set2 = {1,2,3}
set1.update(set2)
print(set1)          #Output: {1, 2, 3, 'blue', 'green', 'red'}

# Keep only duplicate items intersection_update()
x = {"apple", "banana", "cherry"}
y = {"google", "durgesh", "banana"}
x.intersection_update(y)
print(x)        #Output:{'banana'}

# Intersection method with return a new set for common or duplicate items.
x = {"apple", "banana", "cherry"}
y = {"google", "durgesh", "banana"}
z = x.intersection(y)
print(z)     #Output:{'banana'}

# Keep all, but NOT the Duplicate or common items
x = {"apple", "banana", "cherry"}
y = {"google", "durgesh", "banana"}
x.symmetric_difference_update(y)
print(x)     #Output:{'durgesh', 'apple', 'cherry', 'google'}

# symmetric_difference() method will return a new set that contain only the elements that are NOT present in Both sets
x = {"apple", "banana", "cherry"}
y = {"google", "durgesh", "banana"}
z = x.symmetric_difference(y)
print(z)          #Output:{'durgesh', 'apple', 'cherry', 'google'}

# ALL PYTHON BUIL-IN SET METHODS   {SUMMARY}
# add()
# clear()
# copy()
# difference()
# difference_update()
# discard()
# intersection()
# intersection_update()
# pop()
# remove()
# union()
# update()
# symmetric_difference()
# symmetric_differnce_update()
