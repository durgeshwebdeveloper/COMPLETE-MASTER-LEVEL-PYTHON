# Syntax for Lambda Arguments : expression 

x = lambda a : a + 10 
print(x(5))   # Output: 15

# Lambda function can even take multiple arguments and return result.
x = lambda  a , b : a + b  
print(x( 5 , 6))     # Output: 11

# 3 arguments in lambda function
x = lambda a, b, c : a + b + c 
print(x ( 5, 6, 2))        # Output:13

# Why use lambda function
def myfunc(n):
    return lambda a: a * n 
mydouble = myfunc(2)
print(mydouble(11))         # Output:22

# New function for double and triple 
def func(n):
    return lambda a : a * n 
mydouble = myfunc(2)
mytriple = myfunc(3)

print(mydouble(11))    # Output:  22
print(mytriple(11))    # Output:  33