password=""
while password != "password123":
    password = input("Enter the password :")
    if password == "password123":
        print("You are logged in!")
    else:
        print("Incorrect password, try again!")
