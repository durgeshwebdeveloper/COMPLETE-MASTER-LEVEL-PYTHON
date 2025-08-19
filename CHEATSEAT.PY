'''            PYTHON CHEATSEAT 
"Python Cheatseat for all python developers"
By Durex Durgesh'''

'''Basics 
Basic Syntax from the Python Programming language '''

'''1. Showing Output to User 
The print function is used to display or print output as follows:'''
print("Content that you wanna print on a screen")

# We can display the content present in an object using the function as follows:
var1 = "Durgesh"
print("Hi my name is : ", var1)

'''2. Taking Input From the User '''
# (i) The input function is used to take input as a string or character from the user as follows:
var1 = input("Enter your name: ")
print("My name is : ", var1)

# (ii) To take input in the form of other data types, we need to typecast them as follows: 
# To take input as an integer:
var1 = int(input("Enter the integer values"))
print(var1)

# (iii) To take input as a float(decimal):
var1 = float(input("Enter the float value"))
print(var1)

'''3. range Function 
The range function returns a sequence of numbers, e.g., numbers starting from 0 to n-1 for range(0, n):#=> range(int_start_value, int_stop_value, int_step_value)
-> Here the start value and step value are by default 1 if not mentioned by the programmer, but int_stop_value
is a compulsory parameter in the range function.
Example: 
Display all even numbers between 1 to 100:'''
for  i in range(0, 101, 2):
    print(i)  # All  Even Numbers between 0 to 100{ zero also included in them}

'''4. Comments 
Comments are used to make the code more understable for progrmmers, and they are not executed by the compiler
of interpreter.'''
# (i) Single Line Comment { Ctrl + /}
# This is a single line comment 

# (ii) Multi-line Comment 
'''This is a 
multi-line
comment'''

'''5. Escape Sequence 
An escape sequence is a sequence of characters that doesn't represent itself but is trasnlated into another 
character when used inside a string literal or character. 
Some of the escape sequence characters are as follows:'''
# (i) Newline 
# Newline Character:
print("\n")

# (ii) Backlslash
# It adds a backslash:
print("//")
 
# (iii) Single Quote 
# It adds a single quotation mark:
print("\'")

# (iv) Tab 
# It gives a tab space: 
print("\t")

# (v) Backspace
# It adds a backspace:
print("\b")

# (vi) Octal Value 
# It  represent the value of an octal number:
print("\ooo")

# (vii) Hex Value 
# It represents the value of a hex number.
print("\xhh")

# (viii) Carriage Return 
# Carriage retrun of \r will just work as if have shifted your cursor to the beginning of the string or line:
print("\x")

'''6. Strings 
Python string is a sequence of characters, and each character can be individually accessed using its index.'''
# String 
# You can create strings by enclosing text in both forms of quotes-single quotes or double quotes: