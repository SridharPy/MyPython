file=open("Sample.txt",'r')
print(type(file))
content=file.read()
print(content, ", Type is : ", type(content))
#file.close()

print("Reading file content as list")
#file1 = open("Sample.txt",'r')
#seek(0) moves the pointer to start of first line in the file
file.seek(0)
content = file.readlines()
print(content , ", Type is : ", type(content))
content=[i.rstrip("\n") for i in content]
print("removed new line character :", content )
#file.close()
