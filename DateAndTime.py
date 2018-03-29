#to format date time into a string check http://strftime.org/
import datetime
import time

#Create a file with timestamp as its name and in txt format
def createlogwithCurDate(filename):
    with open(filename.strftime("%Y-%m-%d__%H-%M-%S")+".txt",'w') as file:
        file.write("This is a file created with timestamp as name")
#Calculates timedifference between two dates
def timeDiff(c,f):
    delta = f - c
    print(delta) #prints actual time difference
    print(delta.days) #prints differnce in days
    print(delta.total_seconds()) #prints diffrence in seconds

def timeAdd(c):
    newDay1= c + datetime.timedelta(days=2) #Adding 2 days to current time stamp
    newDay2 = c + datetime.timedelta(seconds=84600) # Adding 84600 seconds to current time
    print(newDay1)
    print(newDay2,"\n")

currentTime= datetime.datetime.now()
futureTime= datetime.datetime(2019,10,17,16,0,0)
timeDiff(currentTime,futureTime)
timeAdd(currentTime)
filename = datetime.datetime.now()
createlogwithCurDate(filename)

#Using time module to create a set of files at an interval fo 1 second
lst = []
for i in range(5):
    lst.append(datetime.datetime.now())
    time.sleep(1)
    print(lst[i])
