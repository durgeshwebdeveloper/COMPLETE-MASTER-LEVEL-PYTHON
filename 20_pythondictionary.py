# Loop through the dictionary
durgesh = {
    "brand": "ford",
    "model": "xyz",
    "year" : 2020
}
for i in durgesh:
    print(i)  #Output:brand
                       #model
                        #year

# With looping print all the values in the dictionary , one by one 
durgesh = {
    "brand": "ford",
    "model": "xyz",
    "year": 2020
}
for i in durgesh:
    print(durgesh[i])  #Output:ford
                               #xyz
                               #2020

# Values() method to return values of a dictionary.
durgesh = {
    "brand": "ford",
    "model": "xyz",
    "year": 2020
}
for i in durgesh.values():
    print(i)     #Output:ford
                               #xyz
                               #2020

# keys() method to return the key of the dictionary.
durgesh = {
    "brand":"ford",
    "model":"xyz",
    "year": 2020
}
for i in durgesh.keys():
    print(i)    #Output:brand
                       #model
                        #year
            
# Now loop through both the keys and values , by using the items() method.
durgesh = {
    "brand": "ford",
    "model": "xyz",
    "year": 2020
}
for i, y in durgesh.items():
    print(i , y)        #Output:brand ford
                               #model xyz
                               #year 2020
                            
# How to copy the dict.
durgesh = {
    "brand":"ford",
    "model": "xyz",
    "year": 2020
}
durgesh1 = durgesh.copy()
print(durgesh1)             #Output:{'brand': 'ford', 'model': 'xyz', 'year': 2020}

# Another way to make copy is to use dict().built in function.
durgesh = {
    "brand":"ford",
    "model": "xyz",
    "year": 2020
}
durgesh1 = dict(durgesh)
print(durgesh)                #Output:{'brand': 'ford', 'model': 'xyz', 'year': 2020}

# Nested dictionary, a dict can able to contain another dictionary.
myfamily = {
    "child1": {
        "name": "ram",
        "year": 10
    },
    "child2":{
        "name": "laxman",
        "year":8
    },
    "child3":{
        "name": "bharat",
        "year": 6
    }
}
print(myfamily)   #Ouput:{'child1': {'name': 'ram', 'year': 10}, 'child2': {'name': 'laxman', 'year': 8}, 'child3': {'name': 'bharat', 'year': 6}}

# If you want to add 3 dictionary into a new dictionary
child1 = {
    "name":"ram",
    "year":10
},
child2 = {
    "name": "laxman",
    "year":8
},
child3 = {
    "name":"bharat",
    "year":6
}
myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}
print(myfamily)   #Output:{'child1': ({'name': 'ram', 'year': 10},), 'child2': ({'name': 'laxman', 'year': 8},), 'child3': {'name': 'bharat', 'year': 6}}

# PYTHON DICTIONARY METHODS()   {SUMMARY}
# clear()
# copy()
# get()
# items()
# keys()
# fromkeys()
# pop()
# update()
# values()


'''LIST => [] => CHANGEABLE
   TUPLE =>  () => FIXED
   SET => {} => UNIQUE
   DICTIONARY => KEY: VALUE PAIR'''