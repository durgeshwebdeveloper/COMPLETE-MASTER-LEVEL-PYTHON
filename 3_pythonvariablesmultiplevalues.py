# Many values to Multiple Variables

x = "orange"
y = "banana"
z = "apple"
print(x)    #Ouput:orange
print(y)    #Ouput:banana
print(z)    #Ouput:apple

x, y, z = "orange", "banana", "apple"
print(x)   #Ouput:orange
print(y)   #Ouput:banana
print(z)   #Ouput:apple

x = "orange"
y = "banana"
z = "apple"
print(x)  #Ouput:orange
print(y)  #Ouput:banana
print(z)  #Ouput:apple

x = y = z = "orange"
print(x)   #Ouput:orange
print(y)   #Ouput:orange
print(z)   #Ouput:orange

fruits = ["orange","banana", "apple"]
x, y, z = fruits
print(x)   #Ouput:orange
print(y)   #Ouput:banana
print(z)   #Ouput:apple

#Output Variable

x = "My name is Durgesh"
print(x)   #Ouput:My name is Durgesh

x = "My"
y = "name"
z = "is Durgesh"
print(x, y, z)   #Ouput:My name is Durgesh

x = "My"
y = "name"
z = "is Durgesh"
print(x + y + z)    #Ouput:My name is Durgesh

x = 5 
y = 10
z = 15
print(x + y + z)   #Ouput:30
