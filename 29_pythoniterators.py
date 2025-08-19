# An iterator is an object which implements the iterators protocol, which cosist of the 2 methods:   
#            __iter__()    and   __next__()

# Iterators v/s Iterable 
# All of the 4 data types i.e . list, set, dictionary and tuples are iterators 
# Iterators Methods

durgesh = ("apple", "banana", "cherry")
isdurgesh = iter(durgesh)
print(next(isdurgesh))   #Output: apple
print(next(isdurgesh))   #Output: banana
print(next(isdurgesh))   #Output: cherry

#  A new Example
durgesh = "banana"
datacode = iter(durgesh)
print(next(datacode))    #Output: b
print(next(datacode))    #Output: a
print(next(datacode))    #Output: n
print(next(datacode))    #Output: a
print(next(datacode))    #Output: n
print(next(datacode))    #Output: a

# Looping through an iterator 
durgesh = ("apple", "banana", "cherry")
for i in durgesh:
    print(i)    #Output: apple   banana   cherry

# Looping through a string as iterate
durgesh = "banana"
for i in durgesh:
    print(i)    #Output:   b    a   n   a    n     a

# Create an Iterators 
# to create an object or class you will have to implement   __iter__()   and   __next__() to object. 
# all classes have a functions which is called __init__(), which allows you to do some initialization.

# Example for better understanding 
class mynumber:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a 
        self.a += 1
        return x 
myclass = mynumber()
myiter = iter(myclass)
print(next(myclass))   #Output: 1
print(next(myclass))   #Output: 2 
print(next(myclass))   #Output: 3
print(next(myclass))   #Output: 4
print(next(myclass))   #Output: 5

# Stop iteration - to prevent the iteration to go over forever, we use the StopIteration statement
class mynumber:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a 
            self.a += 1
            return x 
        else:
            raise StopIteration
myclass = mynumber()
myiter = iter(myclass)
for i in myiter:
    print(i)    #Output: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

    



