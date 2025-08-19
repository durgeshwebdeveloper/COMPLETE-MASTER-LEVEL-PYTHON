# Built - In Data Types

'''Text type : str 
Numeric types : int, float, complex 
Sequence Type : List , Tuple , range
mapping : dict 
set type : set, frozenset 
boolean type : bool
Binary type : bytes , bytearray, memoryview'''

x = 5
y = "Durgesh"

print(type(x))    #Ouput:<class 'int'>
print(type(y))    #Ouput:<class 'str'>

x = "Durex Durgesh"   #Ouput:str
x = 20  #int
x = 20.5   #float
x = 1j  #complex
x = ["Durgesh", "Durex"]   #Ouput:List
x = ( " Durgesh", "Durex")  #Ouput:tuple
x = range(5)
x = {"name" : "Durgesh", "age": "50"}  #dOuput:ict
x = {"apple", "banana", "orange"}  #Ouput:set
x = True  #Ouput:bool
x = b"durgesh"  #Ouput:bytes
x = bytearray(5)  #Ouput:bytearray
x = memoryview(bytes(5))   #Ouput:memoryview

# Setting out the specific Data Type

x = str("Durex Durgesh")
x = int(20)
x = float(20.5)
x = complex(1j)
x = list(("orange", "sdsdsd"))
x = tuple(("apple", "banana"))
x = range(5)
x = dict(name = "durgesh", age = 23)
x = set("apple", "banana")
x = frozenset(("apple", "durgesh"))
x = bool(12)
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))