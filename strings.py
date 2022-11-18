# the conversation of character to a number is called encoding, and the reverse is decoding. ASCII and Unicode are common encoding types
# In python strings are unicode

my_name = "Jacob"
my_nick_name = "Jake"
my_info = """I am an active duty officer
in the Air Force
"""
print(f'My name is {my_name}, I go by {my_nick_name}, and {my_info}')

# spaces are preserved
my_str = ""
my_str_1 = " "
print(f'{bool(my_str)}, {bool(my_str_1)}')

# accessing chars in a string, slicing operations
print(my_name[0]) #first char
print(my_name[-1]) #last char
print(my_name[1:]) #everything but the first char
print(my_name[:4]) #everythign up to the 4th char

# strings are immuntable, cannot change the elements of a string only reassign a different string to the same name

# case conversion
my_str = "PyThonscripTing"
print(my_str.lower())
print(my_str.upper())
print(dir(my_str)) #shows available operations for the string
print(my_str.swapcase())
print(my_str.title()) #first letter of each word capitalize
print(my_str.capitalize()) #only first letter in string
print(my_str.casefold()) #same as lower

# boolean operations
print(my_str.lower().startswith("p")) # case sensitive
print(my_str.lower().endswith("ting"))
print(my_str[13:].islower())
print(my_str.isspace())
print(my_str.isalpha())
# help(str) to get documentation on str operations

str2 = "python"
str3 = "-".join(str2)
print(str3)

str4 = "python scripting"
str5 = "str ops"
print(f"{str2.center(20)}\n{str4.center(20)}\n{str5.center(20)}")

print(str2.zfill(10))

#strip and split
str6 = " python "
str7 = "python"
print(str6.strip()) #remotes leading and trailing spaces
print(str7.strip("py"))
str8 = "xpythonx"
print(str8.rstrip("x")) #only strips on right side
str9 = "python./i"
print(str9.strip("./i"))
str10 = "pythonyy"
print(str10.strip("p").rstrip("y"))

str11 = "python is fun"
print(str11.split()) #['python', 'is', 'fun']
print(str11.split("is")) #['python ', ' fun']

# count, index, find
str12 = "python is fun and it is popular"
print(str12.count("is")) #2
print(str12.index("p")) #0 - returns index of first result from left to right
print(str12.index("p", 1)) #24 - look from an index, if doesnt find then returns error
print(str12.find("p", 28)) #-1 returns -1 if doesnt find

