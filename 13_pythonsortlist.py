# Sort the list alphabetically
x =[ "orange", "mango", "kiwi", "pineapple", "banana"]
x.sort()
print(x)    # Output:['banana', 'kiwi', 'mango', 'orange', 'pineapple']

# Sort the list numerically
x= [100, 50,65, 82, 23]
x.sort()
print(x)      # Output:[23, 50, 65, 82, 100]

# Sorting the list in decreasing order.
x = ["orange","mango", "kiwi", "pineapple", "banana"]
x.sort(reverse=True)
print(x)      # Output:['pineapple', 'orange', 'mango', 'kiwi', 'banana']

# Sorting the list numeric in decresing order
x =[ 100, 50,65, 82, 23]
x.sort(reverse=True)
print(x)        # Output:[100, 82, 65, 50, 23]

# Customize sort funcitons
def myfuncn(n):
    return abs(n-50)
x = [100,50,65, 82, 23]
x.sort(key = myfuncn)
print(x)         # Output:[50, 65, 23, 82, 100]

# Reverse the sorting order
x = [ "orange", "mango", "kiwi", "pineapple", "banana"]
x.reverse()
print(x)          # Output:['banana', 'pineapple', 'kiwi', 'mango', 'orange']

# How to Copy a list
x = [ "orange", "mango", "kiwi", "pineapple", "banana"]
y = x.copy()
print(y)           # Output:['orange', 'mango', 'kiwi', 'pineapple', 'banana']

# Make a copy of list with built in method
x = ["orange", "mango", "kiwi","pineapple","banana"]
y = list(x)
print(y)               # Output:['orange', 'mango', 'kiwi', 'pineapple', 'banana']

# Joining the List
x = ["orange", "mango", "kiwi", "pineapple","banana"]
y = [ 1,2,3,4,5]
z = x + y
print(z)            # Output:['orange', 'mango', 'kiwi', 'pineapple', 'banana', 1, 2, 3, 4, 5]

# Another way joining through append()
x = ["orange", "mango", "kiwi", "pineapple", "banana"]
y = [1,2,3,4,5]
for i in y:
    x.append(i)
print(x)                # Output:['orange', 'mango', 'kiwi', 'pineapple', 'banana', 1, 2, 3, 4, 5]

# Another way of joining through extend()
x = [ "orange", "mango", "kiwi", "pineapple", "banana"]
y = [1,2,3,4,5]
x.extend(y)
print(x)              # Output:['orange', 'mango', 'kiwi', 'pineapple', 'banana', 1, 2, 3, 4, 5]

# LIST METHOD { SUMMARY }
# append()
# clear()
# copy()
# Count()
# extend()
# index()
# insert()
# pop()
# remove()
# reverse()
# sort()