name = "admin"
password = "1234"

username = input("Please enter your username: ")
user_password = input("Please enter your password: ")

if (username == "admin" and user_password == "1234"):
    print("Access granted")
else:
    print("Access denied")
    print("Incorrect username or password")