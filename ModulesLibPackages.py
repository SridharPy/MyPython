#Module is a single python script e.g. os and needs to be imported as these are not loaded by default at python start up
#Library is a collection of python scripts and these needs to be imported as well e.g. sqlite3
#Package is a third party library, we need to install them using pip e.g. pip install glob2 and then they can be imported just like built in library like import glob 2

#importing os module
import os
print("\nModules Example : OS")
print("\nlists all the files in current directory")
print(os.listdir())
print("\nAll the methods of OS module")
print(dir(os),"\n")
print("\nThe path of the os module")
print(os.__file__)
print("\nProvides basic information provided in teh doc string of os module by the developer")
print(os.__doc__)
#importing library
import sqlite3
print("\nAll the methods of sqllite3 library")
print(dir(sqlite3))

#importing package glob2 installed from commandline "pip install glob2"
import glob2
print("\nAll the files in the current directory")
print(glob2.glob("*"))
print("\nList only the txt files in current directory")
print(glob2.glob("*.txt"))
