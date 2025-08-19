# JSON is a syntax for storing and exchanging the data, it is text which is written with JavaScript  object notation. 
# Convert from JSON to python 
import json 
x = '{"name": "durgesh", "age": 36, "city": "Raipur"}'
y = json.loads(x)

# The result will be in python dictionary 
print(y["age"])   #Output: 36

# Converting from python to json 
import json 
x = { "name": "durgesh", "age":38, "city": "delhi"}

# converting into json
y = json.dumps(x)

# The result will be in string
print(y)    #Ouput:{"name": "durgesh", "age": 38, "city": "delhi"}

# You can convert the following python object to json strings.
# dict, list, tuples, string, int, float, true, false, none 
import json
print(json.dumps({"name":"durgesh", "age":39, "city": "delhi"}))    #Output:{"name": "durgesh", "age": 39, "city": "delhi"}
print(json.dumps(["apple", "banana"]))      #Output:["apple", "banana"]
print(json.dumps(("durgesh", "durex")))      #Output:["durgesh", "durex"]
print(json.dumps("hello"))       #Output:"hello"
print(json.dumps(42))          #Output:42
print(json.dumps(31.43))     #Output:31.43
print(json.dumps(True))      #Output:true
print(json.dumps(False))     #Output:false
print(json.dumps(None))     #Output:null

# When you convert from python to json then python objects are converted into JavaScript json.
import json
x = {"name":"durgesh", "age": 36, "married"
     :True, "divoced": False, "children"
     : ("lichi","chiku"), "pets":None, "cars"
     :[{"model": "bmw230","mpg":22.5}, 
     {"model":"ford echo", "mpg":24.1}]}

# Converting into json 
y = json.dumps(x)
print(y)      #Output:{"name": "durgesh", "age": 36, "married": true, "divoced": false, "children": ["lichi", "chiku"], "pets": null, "cars":     [{"model": "bmw230", "mpg": 22.5}, {"model": "ford echo", "mpg": 24.1}]}

# how to format the result
import json 
x = {"name":"durgesh", "age": 36, "married"
     :True, "divoced": False, "children"
     : ("lichi","chiku"), "pets":None, "cars"
     :[{"model": "bmw230","mpg":22.5}, 
     {"model":"ford echo", "mpg":24.1}]}
 
 # Using the 4 indents to make it easier to read
print(json.dumps(x, indent=4))     
'''Output:
{
    "name": "durgesh",
    "age": 36,
    "married": true,
    "divoced": false,
    "children": [
        "lichi",
        "chiku"
    ],
    "pets": null,
    "cars": [
        {
            "model": "bmw230",
            "mpg": 22.5
        },
        {
            "model": "ford echo",
            "mpg": 24.1
        }
    ]
}
   '''

# You can also define the separators meaning comma, colon, space.
import json 
x = {"name":"durgesh", "age": 36, "married"
     :True, "divoced": False, "children"
     : ("lichi","chiku"), "pets":None, "cars"
     :[{"model": "bmw230","mpg":22.5}, 
     {"model":"ford echo", "mpg":24.1}]}

print(json.dumps(x, indent=4, separators=(".","=")))    
'''Output:
{
    "name"="durgesh".
    "age"=36.
    "married"=true.
    "divoced"=false.
    "children"=[
        "lichi".
        "chiku"
    ].
    "pets"=null.
    "cars"=[
        {
            "model"="bmw230".
            "mpg"=22.5
        }.
        {
            "model"="ford echo".
            "mpg"=24.1
        }
    ]
}'''


# # Also you can get the result in specified order
import json 
x = {"name":"durgesh", "age": 36, "married"
     :True, "divoced": False, "children"
     : ("lichi","chiku"), "pets":None, "cars"
     :[{"model": "bmw230","mpg":22.5}, 
     {"model":"ford echo", "mpg":24.1}]}
print(json.dumps(x, indent=4, sort_keys= True, separators=(".", "=")))    
'''Output: 
{
    "age"=36.
    "cars"=[
        {
            "model"="bmw230".
            "mpg"=22.5
        }.
        {
            "model"="ford echo".
            "mpg"=24.1
        }
    ].
    "children"=[
        "lichi".
        "chiku"
    ].
    "divoced"=false.
    "married"=true.
    "name"="durgesh".
    "pets"=null
}'''