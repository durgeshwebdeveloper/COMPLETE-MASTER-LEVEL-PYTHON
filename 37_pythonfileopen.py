# File Handling - open()
f = open("demofile.txt")
   # or
f = open("demofile.txt", "rt")

# There are 4 different modes of opening file
# "r", "a", "w", "x"

# To open the file using built in open() and read()
f  =  open("demofile.txt", "r")
print(f.read())       #output: hello baby kaise ho maje mein ho na 
                              #   Aur kya haal DurexDurgesh bhai
                 

# # Open the file in different location 
f = open(r"C:\Users\iitia\OneDrive\Documents\COMPLETE  MASTER LEVEL PYTHON\demofile.txt", "r")
print(f.read())          #output: hello baby kaise ho maje mein ho na 
                              #   Aur kya haal DurexDurgesh bhai
                 
# # Read only parts of the file 
f =open(r"C:\Users\iitia\OneDrive\Documents\COMPLETE  MASTER LEVEL PYTHON\demofile.txt", "r")
print(f.read(7))      #output:  hello b

# # How to read lines 
f = open(r"C:\Users\iitia\OneDrive\Documents\COMPLETE  MASTER LEVEL PYTHON\demofile.txt", "r")
print(f.readline())         #output: hello baby kaise ho maje mein ho na
print(f.readlines())        #output:  [' Aur kya haal DurexDurgesh bhai']
 
# # Looping through the line by line 
f = open(r"C:\Users\iitia\OneDrive\Documents\COMPLETE  MASTER LEVEL PYTHON\demofile.txt", "r")
for i in f:
    print(i)      #Output: hello baby kaise ho maje mein ho na
                         #  Aur kya haal DurexDurgesh bhai

# # How to close th eopen file 
f = open(r"C:\Users\iitia\OneDrive\Documents\COMPLETE  MASTER LEVEL PYTHON\demofile.txt","r")
print(f.readline())     #output: hello baby kaise ho maje mein ho na
f.close()