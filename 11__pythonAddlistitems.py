# Append()
x= ["apple", "Banana", "orange"]
x.append("cherry")
print(x)      #Output:['apple', 'Banana', 'orange', 'cherry']

# Insert()
x = ["apple","banana", "orange"]
x.insert(1,"cherry")
print(x)     #Output:['apple', 'cherry', 'banana', 'orange']

# Extend()
x = ["apple", "banana", "orange"]
y = [ "mango", "pineapple", "papaya"]
x.extend(y)
print(x)      #Output:['apple', 'banana', 'orange', 'mango', 'pineapple', 'papaya']

# Remove List Items
x = ["apple", "banana", "orange"]
x.remove("banana")
print(x)        #Output:['apple', 'orange']

# Remove Specified Index
x  = [" apple", "banana", "orange"]
x.pop(1)
print(x)       #Output:[' apple', 'orange']

# Remove last index without knowing the length
x = [ " apple", "banana", "orange"]
x.pop()
print(x)      #Output:[' apple', 'banana']

# Using Del for specified index
x = ["apple", "banana" , "orange"]
del x[0]
print(x)    #Output:['banana', 'orange']

# Deleting list completely
x = [ "apple", "banana", "orange"]
del x

# Clear the List method
x = [ " apple", "banana" , "orange"]
x.clear()
print(x)    #Output:[]