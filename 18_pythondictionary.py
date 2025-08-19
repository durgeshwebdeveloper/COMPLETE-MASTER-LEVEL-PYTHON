# Definition of Dictionary
durgesh = {
    "brand": "ford",
    "model": "DT",
    "year":2020
}
print(durgesh)   #Ouput: {'brand': 'ford', 'model': 'DT', 'year': 2020}

# If you want to print "brand" value from the dictionary
durgesh = {
    "brand":"ford",
    "model":"DT",
    "year":2022
}
print(durgesh["brand"])     #Ouput: ford

# Duplicate not allowed
durgesh = {
    "brand": "ford",
    "model": "DT",
    "year":2022,
    "year":2022
}
print(durgesh)             #Ouput: {'brand': 'ford', 'model': 'DT', 'year': 2022}

# How to find dictionary length
durgesh = {
    "brand":"ford",
    "model":"DT",
    "year": 2020,
    "year": 2022
}
print(len(durgesh))             #Ouput: 3

# Dictionary Items - Data type
durgesh = {
    "brand":"ford",
    "model":"DT",
    "year":2020,
    "color": ["red","white","blue"]
}
print(durgesh)       #Ouput:{'brand': 'ford', 'model': 'DT', 'year': 2020, 'color': ['red', 'white', 'blue']}

# How to know the Type of Function
durgesh = {
    "brand":"ford",
    "model":"DT",
    "year":2020,
    "color":["red","white","blue"]
}
print(type(durgesh))       #Ouput:<class 'dict'>

# Accessing items of Dictionary
durgesh = {
    "brand": "ford",
    "model": "DT",
    "year": 2020,
    "color": ["red","white", "blue"]
}
x = durgesh["model"]
print(x)        #Ouput:DT

# Accessing items of dictionary through get()
durgesh = {
    "brand":"ford",
    "model":"DT",
    "year": 2020,
    "color": ["red", "white", "blue"]
}
x = durgesh.get("model")
print(x)                 #Ouput:DT

# key() methods will return all the keys in the dictionary
durgesh  = {
    "brand": "ford",
    "model": "DT",
    "year":2020,
    "color": ["red", "white", "blue"]
}
x = durgesh.keys()
print(x)                      #Ouput:dict_keys(['brand', 'model', 'year', 'color'])

# Adding keys and values items to the original dictionary
durgesh = {
    "brand":"ford",
    "model": "DT",
    "year": 2020
}
x = durgesh.keys()
print(x)   #before the change
# Output:dict_keys(['brand', 'model', 'year'])
durgesh["color"] = "white"
print(x)    # after the change
#Ouput:dict_keys(['brand', 'model', 'year', 'color'])

#How to get the values of dictionary
durgesh = {
    "brand": "ford",
    "model": "DT",
    "year": 2020,
}
x = durgesh.values()
print(x)                #Ouput:dict_values(['ford', 'DT', 2020])

# Adding values and keys items to the origianal dictionary
durgesh = {
    "brand": "ford",
    "model": "DT",
    "year": 2020
}
x = durgesh.items()
print(x)       #before the change     
#Output: #dict_items([('brand', 'ford'), ('model', 'DT'), ('year', 2020)])
durgesh["color"] = "red"
print(x)   #after the change
# Output:dict_items([('brand', 'ford'), ('model', 'DT'), ('year', 2020), ('color', 'red')])

# How to get each items in a dictionary as tuples tn the list
durgesh = {
    "brand":"ford",
    "model": "DT",
    "year":2020
}
x = durgesh.items()
print(x)             #Output:dict_items([('brand', 'ford'), ('model', 'DT'), ('year', 2020)])

# Check if the keys exists.
durgesh  = {
    "brand": "ford",
    "model": "DT",
    "year":2020
}
if "model" in durgesh:
    print("Yes, 'model' is present in the durgesh.")     #Ouptput:Yes, 'model' is present in the durgesh.