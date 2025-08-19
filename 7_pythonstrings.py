x = "durgesh"
y = 'durgesh'
print(x)    #Output: durgesh
print(y)    #Output: durgesh

# Single Line String 
x ="Durgesh"

# Multiline String

z = '''Twinkle Twinkle little star how i wonder what you are'''
print(z)    #Output: Twinkle Twinkle little star how i wonder what you are

#Strings are Arrays
a = "Durgesh Durex"
print(a[1])  #Output: u

# Looping through the string
for x in "banana":
    print(x)   #Output: b
                       # a
                       # n
                       # a
                       # n
                       # a
# String Length 
a = '''Durgesh Gupta ji kaise ho aap '''
print(len(a))   #Output:30

# Check String 
txt = "In this tutorial everything is free."
print("free" in txt)   # Output: Tru

# Check String with If for user friendly
txt = "In this tutorial everything is free"
if "free" in txt:
    print("Yes, 'free' is present")   #Output:Yes, 'free' is present

# Check if "free is not present"
txt = "In this tutorial everything is free"
print("durgesh" not in txt)  #Output: True

# Print only if "durgesh" is not present

txt = "In this tutorial everything is free "
if "durgesh" not in txt:
    print("No, 'durgesh' is Not Present")    #Output: No, 'durgesh' is Not Present
