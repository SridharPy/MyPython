"""This python program allows to open and write to a file"""

file=open("samplewrite.txt",'w')
file.write("This is first line \n")
file.write("This is second line \n")
file.close()
file=open("samplewrite.txt",'r')
print(file.read())
file.close()

#using For loop to write multiple lines to a file
file=open("sampleforwrite.txt",'w')
lst=["items", "Cost", "Quatity"]
for item in lst:
    file.write(item + "\n")
file.close()
file = open("sampleforwrite.txt",'r')
print(file.read())
file.close()

#Example to append new text into the exisiting file samplewrite.txt
file=open("samplewrite.txt",'a')
file.write("This is third line")
file.close()
file=open("samplewrite.txt",'r')
print(file.read())
file.close()
