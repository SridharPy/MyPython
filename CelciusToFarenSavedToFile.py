
"""These are two function converting supplies list of temperatures in Celcius to Farenheith and saves in a file call FarenValues.txt and temps.txt"""
def c_to_f_file(c):
    if c >= -273.15:
        f= c * 9/5 +32
        file = open("FarenValues.txt",'a+')
        file.write(str(f) +"\n")

temperatures=[10,-20,-289,100]
for t in temperatures:
    c_to_f_file(t)

#Same thing can be achieved by below code,it is better as on each excution the file is overwritten and the values are not added again and again
def writer(temperatures):
    with open("temps.txt", 'w') as file:
        for c in temperatures:
            if c>-273.15:
                f=c*9/5+32
                file.write(str(f)+"\n")
    """converts celsius to farenheit"""

writer(temperatures)
#Here we're calling the function, otherwise no output will be generated
