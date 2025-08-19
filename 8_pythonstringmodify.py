# Upper
a = "durgesh is a bad boy"
print(a.upper())   #Output: DURGESH IS A BAD BOY

# Lower
a = "DURGESH IS A BAD BOY"
print(a.lower())   #Output: durgesh is a bad boy

# Removing Whitespaces{ only start and end wala hi whitespaces remove hota hai beech mein kahi ka nhi hoga }
a = "      Durgesh, Durex    "
print(a.strip())   #Output: Durgesh, Durex

# Replace String 
a = "this is my tutorial"
print(a.replace("this", "bhai"))   #Output: bhai is my tutorial

# Split String
a = "durgesh, durex"
b  = a.split(" ,")
print(b)   #Output:['durgesh, durex']