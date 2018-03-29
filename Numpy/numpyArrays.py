import numpy

#numpy arrays are n dimensional arrays and are different from list
#ligheter on memory and cpu
na = numpy.arange(27)
print(na)
print(type(na))

#Resahpe na to a 2 dimensional array
d2a=na.reshape(3,9)
print("\nTwo Dimensional Array \n",d2a)

#Re-Shape to a 3 dimensional arrays
d3a = na.reshape(3,3,3)
print("\nThreed Dimensional Array \n", d3a)

#Converting a list into munpy arrays
lst = [["a","b","c"],["d","e","f"]]
print("\nNormal List \n",lst)
print(type(lst),"\n")

numAr = numpy.asarray(lst)
print("Converted to Numpy Array \n",numAr)
print(type(numAr))
