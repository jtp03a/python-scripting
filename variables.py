# Practice on how variables are stored in memory 
# python is dynamically typed
# Everything in python is object.
# Python stores object in heap memory and reference of object in stack.
# Variables, functions stored in stack and object is stored in heap.
#  Python interpreter actively allocates and deallocates the memory on the Heap
# Variable Naming Rules: should only contain letters, numbers, and underscore, shouldnt be a predefined word, no spaces, it should not start with a number, they are case sensitive, can start with _
x = 4
print(x)
print(id(x))
print(type(x))
# redeclare
x = 20
print(x)
print(id(x))
# not the same ref in memory
# delete variable
del x
# variable name rules
x = 5
a = 5
print(id(x))
print(id(a))
# points to same object in memory - This is called interning and occurs for small integers, boolean, and some strings
c = 7
d = c
print(id(c))
print(id(d))
# points to same object in memory
e = x + a
print(e)
print(id(e))
# Interning does not occur for large integers, most strings, floats, lists, dicts, and tuples
list_a = []
list_b = []
print(id(list_a))
print(id(list_b))
# different memory address
# lists are mutable, memory address stays the same if you add to it
list_a.append(1)
print(list_a)
print(id(list_a))
# if one list refers to another a change to 1 list will propagate to the other since they refer to the same object in memory
list_c = [1, 2, 3]
list_d = list_c
print(id(list_c))
print(id(list_d))
# same object in memory
list_c[0] = 5
print(list_c)
print(list_d)
# use list to list.copy() to make a seperate object
list_e = list_c.copy()
print(id(list_c))
print(id(list_e))
list_c[1] = 10
print(list_c)
print(list_e)
# is tells you if two objects are pointing to the same object, different from == which tells content or value is the same or not
print(list_c is list_e)
print(list_d is list_c)
list_a = []
list_b = []
print(list_a == list_b)

# Variable Data Types
# data types are actually classes and variables are an instance(object) of these classes
# Basic Types: Number(int, float, complex), Strings, Boolean
x = 3
y = 5.6
z = 3+4j
print(x, type(x))
print(y, type(y))
print(z, type(z))
name = "Jake"
print(name, type(name))
isBoolean = True
print(isBoolean, type(isBoolean))

# Typecasting
x = 56
print(x, type(x), id(x))
y = str(x)
print(y, type(y), id(y))
x = 5.6
print(x, type(x), id(x))
print(int(x), type(x), id(x))
# cant do this my_name = "Jake", int(my_name), will return error
# Boolean conversions
# Any data type can be converted into a boolean bool()
# bool(empty) = False
a = None
b = 0
c = ""
d = []
e = {}
f = ()
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print(bool(f))
# bool(non_empty) = True
# Any data type can be convereted into a string but reverse not always true, num to string, but not string to num unless the string is just a num




