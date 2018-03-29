def convert_celcius_to_farenheit(c):
    f = c * 9/5 + 32
    return f

temperatures=[10,-20,-289,100]

for t in temperatures:
    if t <= -273.15:
        print("That temperature doesn't make sense!")
    else:
        print(convert_celcius_to_farenheit(t))
