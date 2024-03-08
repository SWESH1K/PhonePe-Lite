
'''
                            --PhonePe Functionalties--
                                                        -made by Sweshik - 2310080053
    1, User Authentication
    2, Send Money
    3, Request Money
    4, Check Balance
    5, Transaction history
    6, PayLater System
'''
from Users_Log import users
import datetime
import json

def authenticate(username,password):
    if users[username]["password"]==password:
        print("Login Successfull!")
        return True
    else:
        print("Invalid Password!! Please try again!!!")
        return False
def userLogin():
    username = input("Please enter the username: ")
    if(username not in users): 
        print("Invalid Username!")
        return userLogin()
    password = input("Please enter the password: ")
    if(authenticate(username,password)): return username,password
    else: return userLogin()

def userChoice():
    print("\n")
    functionalities = ["Send Money", "Request Money", "Check Balance", "Transaction History", "Pay Bills"]
    for i in range(len(functionalities)):
        print(i+1,".",functionalities[i])
    try:
        op = int(input("Choose the option (0 to exit): "))
        if(op not in range(6)):
            print("Please enter the valid index!!")
            return userChoice()
        else: return op
    except: 
        print("Please enter the index only!")
        return userChoice()

def getAmount():
    try:
        amount = int(input("Enter the amount: "))
        return amount
    except:
        print("Please enter a valid amount.")
        return getAmount()
    
def getUser():
    username = input("Enter the username: ")
    if username not in users:
        print("User not found!")
        return getUser()
    else: return username

def getPin(username,count=0):
    try:
        pin = int(input("Enter your pin: "))
        if(pin == users[username]["pin"]):
            return True
        else:
            print("Incorrect Pin!",4-count,"attempts left")
            if(count==4):
                print("Limit Exceeded. Please try again later.")
                return False
            return getPin(username,count+1)
    except:
        print("Please enter a valid pin!")
        return getPin(username)

class PhonePe:
    def __init__(self, username, password) -> None:
        self.username = username
        self.__password = password
        self.__balance = users[username]["balance"]
    
    def getBalance(self):
        return print("Current Balance: ",self.__balance)
    
    def sendMoney(self, recipient_username, amount: int):
        print("\n")
        if amount > self.__balance:
            print("Insufficient Balance!")
        else:
            
            if(getPin(self.username) == False): exit()

            print(f"--> {amount} Rs sent to {recipient_username}.")
            # Deduct amount from sender's balance
            users[self.username]["balance"] -= amount
            # Add amount to recipient's balance
            users[recipient_username]["balance"] += amount
            # Update sender's balance
            self.__balance = users[self.username]["balance"]
            # Write updated balance to User_Log file
            try:
                with open("Users_Log.py", "w") as file:
                    file.write("users = " + json.dumps(users, indent=4))
            except Exception as e:
                print("Error updating User_Log:", e)
            # Adding transaction history to Transaction_History.txt
            try:
                with open("Transaction_History.txt", "a") as file:
                    file.write(f"\n{datetime.datetime.now()} --> {self.username} sent {amount}Rs to {recipient_username} --> -{amount}Rs\n")
            except Exception as e:
                print("Error updating Transaction_History:", e)
    
    def requestMoney(self, senders_username,amount: int):
        print("\n")
        print(f"{amount}Rs requested from {senders_username}...")
        if amount > users[senders_username]["balance"]:
            print(f"{senders_username} has refused your request!")
        else:
            print(f"--> {senders_username} send you {amount}Rs.")
            # Deduct amount from sender's balance
            users[senders_username]["balance"] -= amount
            # Add amount to your balance
            users[self.username]["balance"] += amount
            # Updating balance
            self.__balance = users[self.username]["balance"]
            # Write updated balance to User_Log file
            try:
                with open("Users_Log.py", "w") as file:
                    file.write("users = " + json.dumps(users, indent=4))
            except Exception as e:
                print("Error updating User_Log:", e)
            # Adding transaction history to Transaction_History.txt
            try:
                with open("Transaction_History.txt", "a") as file:
                    file.write(f"\n{datetime.datetime.now()} --> {self.username} requested {amount}Rs from {senders_username} --> +{amount}Rs\n")
            except Exception as e:
                print("Error updating Transaction_History:", e)

    def getTransactionsAll(self):
        print("\n")
        print("Transaction History:")
        try:
            with open("Transaction_History.txt", "r") as file:
                for line in file:
                    print(line,end="")
        except Exception as e:
            print("Error reading Transaction_History:", e)

    # Printing the transactions of only a particular user in Transaction_History.txt
    def getTransactionsOfUser(self,username):
        print("\n")
        print(f"Transaction History of {username}:")
        print()
        try:
            with open("Transaction_History.txt", "r") as file:
                for line in file:
                    if username in line:
                        print(line)
        except Exception as e:
            print("Error reading Transaction_History:", e)


    # Function for paying bills 
    def payBills(self):
        bills = ["Water","Electricity","Internet"]
        print("\n")
        print("Pay Bills:")
        for i in range(len(bills)):
            print(f"{i+1}. {bills[i]}",end=" ")
        print()
        try:
            choice = int(input("Enter your choice: "))
            if choice not in range(1,4):
                print("Please enter a valid choice!")
                return self.payBills()
            amount = getAmount()
            if(amount > self.__balance): print("Insufficient Balance!"); return self.payBills()
            if(getPin(self.username) == False): exit()
            self.__balance -= amount

            # Updating balance in Users_Log.py
            users[self.username]["balance"] = self.__balance
            try:
                with open("Users_Log.py", "w") as file:
                    file.write("users = " + json.dumps(users, indent=4))
            except Exception as e:
                print("Error updating User_Log:", e)

            # Adding transaction history to Transaction_History.txt
            try:
                with open("Transaction_History.txt", "a") as file:
                    file.write(f"\n{datetime.datetime.now()} --> {self.username} paid {bills[choice-1]} bill for {amount}Rs --> -{amount}Rs\n")
            except Exception as e:
                print("Error updating Transaction_History:", e)

            print(f"--> {amount}Rs paid for {bills[choice-1]} bill.")

        except:
            print("Please enter a valid choice!")
            return self.payBills()

    def ui_board(self,choice):
        if choice == 1:
            # Priting other usernames in the users list
            print("\nYour Contacts:")
            for user in users:
                if user != self.username:
                    print(user)
            recipient_username = getUser()
            amount = getAmount()
            self.sendMoney(recipient_username,amount)
        elif choice == 2:
            print("Your Contacts:")
            for user in users:
                if user != self.username:
                    print(user)
            recipient_username = getUser()
            amount = getAmount()
            self.requestMoney(recipient_username,amount)
        elif choice == 3:
            self.getBalance()
        elif choice == 4:
            self.getTransactionsOfUser(self.username)
        elif choice == 5:
            self.payBills()
        elif choice == 0:
            print("Thanks for using PhonePe Lite. See you soon.")
        
        if(choice!=0):
            print()
            self.ui_board(userChoice())