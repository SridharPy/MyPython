# val i set to default 100 if no arg is supplied, if supplied val will be overridden by that value
# non-defualt arg must nevere follow a default arg
def convert_to_kilometers(meters,val=1000):
    km= meters/val
    print(km)
#   return km

def convert_to_millimeters(meters,val=1000):
    mm=float(meters)*val
    print(mm)

meters= float(input("Enter distance in meters to be converted to kilo meters :"))
convert_to_kilometers(meters)

m=input("Enter distance in meters to be converted to milli meters: ")
convert_to_millimeters(m)

#Here we are sending 200 to override default argument 100 in the function convert_to_kilometers
print("Overeriding default argument val to 200 from 1000")
convert_to_millimeters(1000,200)
