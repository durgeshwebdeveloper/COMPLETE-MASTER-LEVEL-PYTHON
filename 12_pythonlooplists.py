# Loop through list
list = [ "durgesh", "banana", "orange"]
for i in list:
    print(i)   #Output:durgesh
                       #banana
                       #orange

# Loop through the index number
list = [ " durgesh", "banana" , "orange"]
for i in range(len(list)):
    print(list[i])     #Output:durgesh
                       #banana
                       #orange

# Using a while loop
list = [ "durgesh", "banana", "orange"]
i = 0 
while i < len(list):
    print(list[i])
    i = i + 1      #Output:durgesh
                       #banana
                       #orange

# Looping using list Comprehension
list = [ "durgesh", " banana" , "orange"]
[print(i) for i in list]     #Output:durgesh
#                                     #banana
#                                     #orange

# # List comprehension
fruits = ["durgesh", "banana", "orange", "cherry", "mango", " kiwi"]
newlist = []
for i in fruits:
    if "e" in i:
        newlist.append(i)
print(newlist)   #Output:['durgesh', 'orange', 'cherry']

# List  Comprehension in 1 line code
fruits = [ "dugesh", "banana", "orange", "cherry", "mango", "kiwi"]
newlist = [ i for i in fruits if "e" in i]
print(newlist)    #Output:['durgesh', 'orange', 'cherry']
