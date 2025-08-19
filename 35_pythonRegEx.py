# RegEx - Regular  Expression, is a sequence of characters that forms a search pattern.
# RegEx Module

import re 
txt = "the rain is falling in India"
x = re.search("^the.*India$",txt)
if x:
    print("Yes, match is true")
else:
    print("no match")
# Output:Yes, match is true

'''regex functions
findall()
search()
split()
sub()

Metacharacters
\d- escape character
. - any character(except newline character)
^ - start with 
$ - end with
* - zero or more occurence
+ - one or more occurence
? - zero or one occurence
{}- Exactly the specified number of occurence
| - Either or 
()- capture and group

The findall() function'''
import re 
txt = "the rain in spain"
x = re.findall("in",txt)
print(x)   #Output:['in', 'in', 'in']

# If in findall no condition is given then it will show empty list.
import re
txt = "the rain in spain"
x = re.findall("India",txt)
print(x)   #Output: []

# The search() function
import re
txt  = "the rain in spain"
x = re.search("\s",txt)
print("White space is located in ", x.start())  #Output:White space is located in  3

#When nothing found in search() function
import re
txt = re.search("India",txt)
print(x)

#The split() function
import re
txt = "the rain in spain"
x  =re.split("\s",txt)
print(x)  #Output:['the', 'rain', 'in', 'spain']

#You can control the number of occurence by specifying the maxsplit parameter.
import re
txt = "the rain in spain"
x = re.split("\s",txt,1)
print(x)    #Output:['the', 'rain in spain']

# The sub() function - replaces the matches with the text of your choice.
import re
txt = "the rain in spain"
x = re.sub("\s","5",txt)
print(x)    #Output: the5rain5in5spain

# You can control the number of replacement by specifying the count parameter.
import re
txt = "the rain in spain"
x = re.sub("\s","5",txt,2)
print(x)     #Output: the5rain5in spain

# Match Object
import re
txt = "the rain in spain"
x = re.search("in",txt)
print(x)