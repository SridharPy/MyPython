def weatherStatus(num):
    if num >= 30:
        return "Too Hot!!"
    elif num <= 10 :
        return "Too Cold :)"
    else:
        return "Good Weather"



temp = int(input("Enter current temperature: "))
if temp >= 60:
    print("You must be burnt by now!")
elif temp <= -50:
    print("You must be too frozen to type!")
else:
    print(weatherStatus(temp))
