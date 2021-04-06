import random
import json

database = { }

#   Program entry or first operation
def init():

    print("Welcome to izudadaBank")

    haveAcct = input("Do you have an account with us? yes/no \n").lower()

    if haveAcct == 'yes':
        print("Please Login")
        login()
    elif haveAcct == 'no':
        print("Please Register")
        register()
    else:
        print("You selected an invalid option. \n Please try again.")

def register():
    print("**********Register**********")
    pwdCheck = False    #   Password Checker

    while pwdCheck == False:    #   While looop to check if password is confirmed

        print("Please create an account with izudadaBank")

        #   Getting User details during registration
        firstName = input("Enter your first name: \n ")
        lastName = input("Enter your last name: \n ")
        email = input("Enter your email address: \n ")
        password = input("Enter a password: \n ")
        confirmPwd = input("Confirm your password: \n ")
        deposit = 0

        if str(password) == str(confirmPwd):    #   Check if password match Confirm Password
            pwdCheck = True

            print("--------------------------------------------------------")
        else:
            #   Second Chance to enter and confirm password
            print("\n ")
            print("Password does not match. Enter password and confirm again")

            password = input("Enter a password: \n ")
            confirmPwd = input("Confirm your password: \n ")

            print("-----------------------------")
            
            if str(password) == str(confirmPwd):
                break   #   Break out of the loop not the program
            else:
                #   User couldn't confirm password and has to restart registration
                print("\n ")
                print("Password still doesn't match. Please restart registration")
                print("**********************************************************")


    acctNumber = genAcctNumb()

    database[email] = [firstName, lastName, acctNumber, password, deposit]

    insertRecord()  #   Insert user record into dataBank.json file

    print("Registration Complete, Please login")

    login()

def login():
    print("**********Login**********")

    email = input("Please Enter your email: \n")
    password = input("Please Enter your password: \n")
    
    #   Check if dataBank.json file exists else create it
    try:
        database_file = open("dataBank.json", "r")
        database_file.close()
    except FileNotFoundError:
        database_file = open("dataBank.json", "a")
        database_file.close()

    database_file = open("dataBank.json", "r")
    output = database_file.read()

    if len(output) == 0:
        print("User record not found. Please register")
        register()
    else:
        data = json.loads(output)

    database_file.close()
    
    if email in data and password in data[email]:
        print("Login successful")
        bankOperation(data[email])
    else:
        print("Invalid account details please login") 
        login()


def bankOperation(user):

    print(f"Welcome {user[0]} {user[1]}")

    print("Below are our available services \n  1) Withdrawal \n  2) Deposit \n  3) Complaint \n  4) Logout  \n 5) logout")
    
    option = int(input("Please select an option using any of the above index/number: \n "))

    if option == 1 :
        withdraw(user)
    elif option == 2:
        deposit()
    elif option == 3:
        complaint()
    elif option == 4:
        logout()
    elif option == 5:
        exit()
    else:
        print("Invalid option, please select the correct option")
        bankOperation(user)

def genAcctNumb():
    return random.randrange(1111111111, 9999999999)

#   Function to add user record to dataBank.json file
def insertRecord():

    #   Check if dataBank.json file exists else create it
    try:
        database_file = open("dataBank.json", "r")
        database_file.close()
    except FileNotFoundError:
        database_file = open("dataBank.json", "a")
        database_file.close()

    #   Open json file as "readonly" and Read json database file if it exist

    database_file = open("dataBank.json", "r")    
    new_output = {}
    
    output = database_file.read()
    #   Get existing record in dataBank file, convert to python dictionary for easy update
    if len(output) == 0:
        output = { } 
    else:
        new_output = json.loads(output) 

    database_file.close()   #   Close database file 

    #   Open json file as "writeonly" and update users records
    database_file = open("dataBank.json", "w") #    Write to json database file if it exist
    new_output.update(database)

    #   Update dataBank content with current user
    json.dump(new_output, database_file)
    database_file.close()   #   Close database file


def withdraw(user):
    balance = user[4]
    withdraw = int(input("How much would you like to withdraw? "))

    if balance < withdraw:
        print("Insufficient funds")
    else:
        print(f"Take your cash: {user}")
        balance -= withdraw

        # #   Open json file as "writeonly" and update users records
        # database_file = open("dataBank.json", "w") #    Write to json database file if it exist
        # new_output[user[]].update(database)

        # #   Update dataBank content with current user
        # json.dump(new_output, database_file)
        # database_file.close()   #   Close database file

def deposit():
    print("You are about to make a deposit")

def complaint():
    complaint = input("How may we serve you better? \n")

    print("We have received your complaint and will get back to you in 24hours")

def logout():
    print("Thanks for banking with us, Do have a pleasant day")
    login()

def exit():
    print("Thanks for banking with us, Do have a pleasant day")
    quit()


#   Banking Opretions or Functions Commencement
init()
