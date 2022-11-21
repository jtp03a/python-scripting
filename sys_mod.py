# functions and variables for manipulating the python runtime environment

import sys

# print(dir(sys)) 

# print(sys.platform)
# print(sys.version)
print(sys.path) #path environment variable

# sys.argv - a list of command line arguments passed to a python script, create error handlers to make sure the script is used properly, execute everything that is needed for the script to run with the cli start command

print(sys.argv) # prints a list of arguments that were passed to the cli when the script is run, by default its just going to be the name of the script file

def convert_chars(string, conv_type):
    if conv_type == 'lower':
        output = string.lower()
        return output
    elif conv_type == 'upper':
        output = string.upper()
        return output
    elif conv_type == 'title':
        output = string.title()
        return output
    else:
        print('Invalid converstion type')

if len(sys.argv) != 3:
    print('This script requires a string, and operation type to passed')
    sys.exit()

output = convert_chars(sys.argv[1], sys.argv[2])

print(output)

sys.exit()