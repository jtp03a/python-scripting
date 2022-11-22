# module is a python file, script, program containing definitions and statements ie functions, classes, variables, used for reusability
# help(modules) will show built in modules
# dir(module) will list all the functions and vaiables for a module
# help(module) will show the help for a module

import modules2
# other ways to import, then you can directly use the functions without referencing the module name or use aliases, can also import modules comma separated
from math import *
from math import pi
import math as m

print(modules2.CONST)
print(pi)
print(m.pi)
