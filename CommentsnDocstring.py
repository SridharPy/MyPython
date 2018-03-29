#this is an example of putting a comment in python
"""This is an example of providing a doc string in a pythong program having multiple lines.
This will help in providing some basic information about the code"""

r"""r is used in a python doc string to say /n is th part of doc string and read it
as a part of the row instead of inserting a new line similarly other special chraters can be
added in the docstring"""

#to read a docstring from python module simpley import the module and use modulename.__doc__
import os
print(os.__doc__)

import fileWrite
print(fileWrite.__doc__)

"""To import and reload a user python program the below program needs to be checked in google for importing a user python module
using imp and reload
import imp
imp.reload(function)
function.sum(1,2)
""""
