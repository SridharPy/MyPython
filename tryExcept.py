def division(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Can't divide a number by zero"


print(division(1,0))
print("This was an example showing Try and Excpet Error Handling")
