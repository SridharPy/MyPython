def convert_celcius_to_farenheit(celcius): 
    f=  celcius * 9/5 + 32
    return f

celcius = float(input("Enter current temperature in Celcius to be converted to Farenheit : "))
if celcius < -273.15:
    print("Nothing can exist at that temperature!")
else:
    print(convert_celcius_to_farenheit(celcius))
