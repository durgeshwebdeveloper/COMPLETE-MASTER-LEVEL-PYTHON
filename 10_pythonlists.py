from pickle import FALSE , TRUE


x = ["apple", "banana", "orange"]
print(x)     #Output:['apple', 'banana', 'orange']

# Duplicates values 
x = [ "apple", "banana", "orange", "apple"]
print(x)   #Output:['apple', 'banana', 'orange', 'apple']

# List length

x = ["apple", "banana", "orange"]
print(len(x))    #Output: 3

# List Items - Data Types

x = ["a", "b", "c"]
y = [1,4,5,7,9]
z = [TRUE, FALSE, TRUE]

# A list strings, int and boolean
x = [ "durgesh",35,TRUE, 50, "Male"]
print(type(x))   #Output:<class 'list'>

# Data type for Lists

# A list with strings , int and boolean
x = [ "durgesh", 35, True, 50,"Male"]
print(type(x))     #Output:<class 'list'>

# The List() Constructor 
x = list(("durgesh", 50, True, 50, "Male"))
print(x)   # the double round brackets same as square brackets.
# Output:['durgesh', 50, True, 50, 'Male']

# Python Collection (Arrays)
# 4 types of data types in python:
# 1.List,   2.Tuple,   3.Set,   4.Dictionary

# How to access items.
x = [ "apple","banana", "Orange"]
print(x[1])   #Output:banana

# Range of indexes
x = [" apple", "banana", "orange", "cherry", "Mango", "durgesh"]
print(x[2:5])    #Output:['orange', 'cherry', 'Mango']

# Negative Indexing
x = [ "apple", "banana"," orange", "cherry",  "Mango", "durgesh"]
print(x[-6:-1])     #Output:['apple', 'banana', ' orange', 'cherry', 'Mango']

# Leaving out the start value
x= [ "apple", "banana", "orange", "cherry", "Mango", "durgesh"]
print(x[:4])     #Output:['apple', 'banana', 'orange', 'cherry']

# Leaving out the Ending value
x = [ "apple","banana", "orange", "cherry", "Mango", "durgesh"]
print(x[1:])      #Output:['banana', 'orange', 'cherry', 'Mango', 'durgesh']

# How to check if the items Exists in List 
x = ["apple", "banana", "orange", "cherry", "Mango", "durgesh"]
if "apple" in x:
    print("Yes, 'apple' is in the List")      #Output:Yes, 'apple' is in the List

# change the item value of List
x = ["apple", "banana","orange","cherry","Mango", "durgesh"]
x[1] = "Watermelon"
print(x)  #Output:['apple', 'Watermelon', 'orange', 'cherry', 'Mango', 'durgesh']

# Change a Range of Items values in List
x = ["apple", "banana", "orange", "cherry","Mango", "durgesh"]
x[1:3] = ["Watermelon","Chiku"]
print(x)   #Output:['apple', 'Watermelon', 'Chiku', 'cherry', 'Mango', 'durgesh']

# Change of one value by replacing it with 2 values
x = [ "apple", "banana", "orange", "cherry", "Mango", "durgesh"]
x[1:2] = ["Watermelon", "Nuts"]
print(x)   #Output:['apple', 'Watermelon', 'Nuts', 'orange', 'cherry', 'Mango', 'durgesh']

# Change of 2 values by replacing it with 1 value
x = ["apple", "banana","orange", "cherry", "Mango", "durgesh"]
x[1:3] = ["Watermelon"]
print(x)   #Output: ['apple', 'Watermelon', 'cherry', 'Mango', 'durgesh']