# Python conditions and if Statement
# Equal  => a == b 
# Not Equal  =>  a != b 
# Less than  =>  a  < b
# Greater than => a > b
# Greater than or Equal to => a >= b 
# Less than of Equal to => a <= b

# Example of  if Statement 
a = 33
b = 200
if  b > a:
    print("b is greater than a")   #Output:b is greater than a

# The Elif keyword is python way of saying  if the previous codition is not true then please try the new condition.
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are same")
#Output:a and b are same

# The else catches anything which isn't caught by any preceeding {if and elif} condition.
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are same")
else:
    print("a is greater than b")
#Output:a is greater than b
    

# You can also have an else without elif 
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("now b is not greater than a")
#Output:now b is not greater than a

# Short Hand if
a = 200
b = 33
if  a > b: print("a is greater than b")    #Output:a is greater than b

# Short Hand if....else
a = 2
b = 300
print("yes a is greater than b") if a > b else print("not it is not greater")              #Output:not it is not greater

# One line if else statement with 3 conditions
a = 100
b = 100
print("A") if a > b else print("both are equal") if a == b else print("B")                #Output:both are equal

# And is a logical operator and it is used to combine the conditional statement.
a = 200
b = 33
c = 500
if a > b and c > a :
    print("Both condition are true")              #Output:Both condition are true

# Or is also a logiacal operator and it is used to combine logical operators.
a = 200
b = 33
c = 500
if a > b or a > c :
    print("atleast one of the 2 conditions is true")           #Output:atleast one of the 2 conditions is true

# Nested if statement - you can have if statement inside if statement . (Very important / must read)
x = 41
if  x > 10:
    print("it is above 10, ")
    if x >20:
        print("and it is also above 20")
    else:
        print("but it is not above 20")
#Output:it is above 10, and it is also above 20

# The pass statement - if with any  reason if statemnt has no content then you can pass the statement for avoiding the error in program.
a = 33
b = 200
if b >  a :
    pass