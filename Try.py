from Users_Log import users

def authenticate(username,password):
    if username in users and users[username]["password"]==password:
        return True
    else: return False

username = input("Please enter the username: ")
password = input("Please enter the password: ")

if authenticate(username,password):
    print("Login Successfull")
else: print("Invalid id and password!")