# Print each items of variable in list 
fruits = ["apple",  "banana", "cherry"]
for i in fruits:
    print(i)    #Output: apple banana cherry

# Looping through string 
for i in "banana":
 print(i)           #Output:   b   a  n   a  n   a

# The break statement 
fruits = ["apple", "banana", "cherry"]
for i in fruits:
   print(i)
   if i == "banana":
      break
#Output:apple   banana 
   
# Exit the loop when i is "banana" , but this time the break comes before print. 
fruits = ["apple", "banana" , "cherry"]
for i in fruits:
   if i == "banana":
    break 
   print(i)   #Output:  apple

# The Continue statement 
fruits = ["apple", "banana", "cherry"]
for i in fruits:
   if i == "banana":
      continue
   print(i)   #Output:  apple   cherry

# The range() function
for i in range(6):
   print(i)   # Output: 0  1  2  3  4  5

# Example of some deep range()
for i in range(2,  6):
   print(i)    #Output: 2  3  4  5  

# You can specify value of increment by adding the 3rd parameter.
for i in range(2,  30,  3):
   print(i)  #Output: 2   5   8   11  14  17  20  23  26  29

# Else in for loop
for i in range(6):
   print(i)
else:
   print("Yeei, Finally it finished")  #Output:Yeei, Finally it finished

# Now we will break the loop i in 3 and the else will be garabge now.
for i in range(6):
   if i == 3: break 
   print(i)
else:
   print("Finally finished")
#Output:0   1  2 

# Nested Loops
adj = [ "red", "big", "tasty"]
fruits = [ "apple", "banana", "cherry"]
for i in adj:
   for y in fruits:
      print(i , y)
#Output:   #red apple   
           #red banana
           #red cherry
           #big apple
           #big banana
           #big cherry
           #tasty apple
           #tasty banana
           #tasty cherry

# The pass statement 
for i in [0, 1, 2]:
 pass
