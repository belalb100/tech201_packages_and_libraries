# Modules

# Piece of software that delivers some type of modurality.

# Difference between module and library module reference

import os
import math, datetime, sys

working_dirrectory = os.getcwd()
print(working_dirrectory)

def return_user_id():
    print(os.getpid())

def return_user_name():
    print(os.uname())

print(datetime.date.today())

print(sys.path)

print(math.remainder(1, 5))

## When you are building a program it is really important to think if you need to create a class/object yourself or crete a function and sometimes you don't need to create a function as it might already may be in the Python Library.

# Built in Functions

# Some functions are so useful some are built in.

