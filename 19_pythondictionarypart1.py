# How to change the values of dictionary
durgesh = {
    "brand":"ford",
    "model":"XYZ",
    "year": 2022
}
durgesh["year"]  = 2018
print(durgesh)   #Output: {'brand': 'ford', 'model': 'XYZ', 'year': 2018}

# Update() method
durgesh = {
    "brand":"ford",
    "model":"XYZ",
    "year":2022
}
durgesh.update({"year":"2018"})
print(durgesh)     #Output: {'brand': 'ford', 'model': 'XYZ', 'year': '2018'}

# How to add the items in dictionary
durgesh = {
    "brand":"ford",
    "model":"XYZ",
    "year":2022
}
durgesh["color"] = "red"
print(durgesh)     #Output: {'brand': 'ford', 'model': 'XYZ', 'year': 2022, 'color': 'red'}

# Adding the items with update() method
durgesh = {
    "brand":"ford",
    "model":"XYZ",
    "year":2022
}
durgesh.update({"color": "red"})
print(durgesh)  #Output:{'brand': 'ford', 'model': 'XYZ', 'year': 2022, 'color': 'red'}

# Removing items from the dictionary
durgesh  = {
    "brand":"ford",
    "model": "XYZ",
    "year": 2022
}
durgesh.pop("model")
print(durgesh)           #Output:{'brand': 'ford', 'year': 2022}

# Removing Last inserted item.
durgesh = {
    "brand":"ford",
    "model":"XYZ",
    "year": 2022
}
durgesh.popitem()
print(durgesh)  #Output:{'brand': 'ford', 'model': 'XYZ'}

# Del() keyword removes the items with the specified key name.
durgesh = {
    "brand": "ford",
    "model": "XYZ",
    "year":2022
}
del durgesh["model"]
print(durgesh)   #Output:{'brand': 'ford', 'year': 2022}

# The Del keyword can also delete the whole dictionary
durgesh = {
    "brand":"ford",
    "model":"XYZ",
    "year":2022
}
del durgesh

# clear() method is used to empty the dictionary
durgesh = {
    "brand": "ford",
    "model": "XYZ",
    "year": 2022
}
durgesh.clear()
print(durgesh)   #Ouput:{}