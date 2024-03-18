from PhonePe import *

if __name__ == "__main__":
    print(" "*50,"-"*4,"Welcome to PhonePe Lite","-"*4)
    username,password = userLogin()
    User = PhonePe(username)
    choice = userChoice()
    User.ui_board(choice)