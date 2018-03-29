#The additonal file handling attributes are r+, w+, a+
file=open("samplewrite.txt",'a+')
print(file.read())
file.seek(0)
print(file.read())
file.write("\nThis is fifth line")
print(file.read())
file.close()

file=open("samplewrite.txt",'r+')
print(file.read())
file.write("\nthis is the new added line")
print(file.read())
file.close()

with open("samplewrite.txt",'r+') as file:
    file.write("This is an overwrite")
    #file.seek(0)
    str=file.read()

print(str)
