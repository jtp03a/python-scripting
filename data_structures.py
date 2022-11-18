# Data structures are used to store a collection of data
# 4 Build in data structures - List [], Tuple (), Dictionary {key:value}, Set {} 
# Lists
mylist = [1, 2, 3, "python", 3.1]
print(mylist, type(mylist))
print(mylist[3], type(mylist[3]))
print(mylist[-1], mylist[-2])
print(mylist[3][0]) #p 
print(mylist[2:4]) # [3, 'python']
print(mylist, mylist[:], mylist[0:]) #same result

# Lists are mutable
print(id(mylist[0]))
mylist[0] = 45
print(mylist)
print(id(mylist[0]))

# list operations
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', 
# '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
# '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 
# 'pop', 'remove', 'reverse', 'sort']

mylist2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(dir(mylist2))









