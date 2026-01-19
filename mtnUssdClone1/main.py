import os
import json
from menu import momoMainmenu, momoTransferMenu, momoPayMenu, momoAirtimeBundlesMenu, allowCashOutMenu, financialMenu, myWalletMenu, just4UMenu, MomoAppMenu
accountNumber = "0550002609"

th=[]
MP = "1234"
MomoAmount = 5000
myContacts = {
    "0123456789": "Oforiwaa",
    "9876543210": "Kwame",
    "5556667777": "Abena",
    "0550002609": "Roland"
}
# Program Functions

def clear_screen(): #Clear Screen Function
    os.system('cls' if os.name == 'nt' else 'clear')

def save_data():  #Using JSON to save data into a file
    data = {
        "balance": MomoAmount,
        "pin": MP,
        "contacts": myContacts,
        "history": th
    }
    with open("momo_data.json", "w") as file:
        json.dump(data, file, indent=4)

def load_data():   #Uses JSON to load data from the previously saved file
    global MomoAmount, MP, myContacts, th
    try:
        with open("momo_data.json", "r") as file:
            data = json.load(file)
            MomoAmount = data["balance"]
            MP = data["pin"]
            myContacts = data["contacts"]
            th = data.get('history', [])
    except FileNotFoundError:
        save_data()



def verifyPin():
    print("Enter Pin")
    pin = input("")
    if pin == MP:
        print("Processing Transaction...")
        return True
    else:
        print("Invalid Pin. Transaction Failed.")
        input("Press Enter to continue...")
        clear_screen()
        return False

def momoWalletMenu(amount):
    global MomoAmount
    if amount <= MomoAmount:
        MomoAmount -= amount
        save_data()  # SAVE AFTER BALANCE CHANGE
        print(f"Transaction Successful. New Balance is {MomoAmount}")
        return True
    else:
        print("Insufficient Funds. Transaction Failed.")
        input("Press Enter to continue...")
        clear_screen()
        return False

def changePin():
    global MP
    print("Enter Current Pin")
    currentPin = input("")
    if currentPin != MP:
        print("Incorrect Pin. Cannot change Pin.")
        input("Press Enter to continue...")
        clear_screen()
        return

    print("Enter New Pin")
    newPin = input("")

    if len(newPin) != 4 or not newPin.isdigit():
        print("Pin must be a 4-digit number. Pin change failed.")
        input("Press Enter to continue...")
        clear_screen()
        return
    
    if newPin == currentPin:
        print("New Pin Can Not Be The Same As Old Pin")
        input("Press Enter to continue...")
        clear_screen()
        return

    print("Confirm New Pin")
    confirmPin = input("")

    if newPin != confirmPin:
        print("Pins do not match. Pin change failed.")
        input("Press Enter to continue...")
        clear_screen()
        return

    MP = newPin
    save_data()  # SAVE AFTER PIN CHANGE
    print("Pin changed successfully.")
    input("Press Enter to continue...")
    clear_screen()

def checkIfNumberIsAllowedMTN(phoneNumber):
    phoneNumber_str = str(phoneNumber)
    allowedPrefixes = ["024", "054", "055", "059", "020", "050"]
    return any(phoneNumber_str.startswith(prefix) for prefix in allowedPrefixes)

def checkIfNumberIsAllowedAT(phoneNumber):
    phoneNumber_str = str(phoneNumber)
    allowedPrefixes = ["027", "057", "026", "056"]
    return any(phoneNumber_str.startswith(prefix) for prefix in allowedPrefixes)

def checkIfNumberIsAllowedTelecel(phoneNumber):
    phoneNumber_str = str(phoneNumber)
    allowedPrefixes = ["020","050"]
    return any(phoneNumber_str.startswith(prefix) for prefix in allowedPrefixes)



def addContact():
    print("Enter Phone Number to Add")
    phoneNumber = input("")
    print("Enter Name for the Contact")
    name = input("")
    myContacts[phoneNumber] = name
    save_data()  # SAVE AFTER ADDING CONTACT
    print(f"Contact {name} added successfully.")
    input("Press Enter to continue...")
    clear_screen()

def transferMoneyToOtherNetworksMenu():
    print("Transfer Money to Other Network")
    print("1. AT")
    print("2. Telecel")
    print("3. E-zwitch")
    print("4. G-Money")
    print("5. Zeepay")
    print("6. GhanaPay")
    print("0. Back")

def loansMenu():
    print("Loans")
    print("1. QWIkLOAN")
    print("2. XpressLoan")
    print("3. AhomakaLoan")
    print("4. XtraBalance")
    print("5. XtraCash")
    print("6. EaztCash")
    print("7. Device Pick and Pay Later")
    print("8. BoseaLoan")

def loanMoney():
    global MomoAmount
    print("Enter Amount")
    amount = input("")
    clear_screen()

    print(f"Do you want to proceed with the loan of {amount}? Enter MoMo Pin to confirm.")

    pin = input("")
    if pin == MP:
        print(f"Congratulations! You have successfully taken a loan of {amount}.")
        input("Press Enter to continue...")
        MomoAmount += int(amount)
        save_data()  # SAVE AFTER BALANCE CHANGE
        clear_screen()


# End Of Program Functions

# Main Program
load_data()
clear_screen()

print("Welcome to MTN MoMo Service")
print("---------------------------")
print("1. Log into MoMo")
print("2. Sign Up for MoMo")
print("3. Exit")

userInput = input("")
try:
    userInput = int(userInput)
except ValueError:
    print("Enter a valid input")
    
if userInput != "1" and userInput != "2":
    print("Thank you for using MoMo services")
    exit()
clear_screen()
if userInput == "1":
    print("Enter MoMo Number")
    userInput = input("")
    if userInput == accountNumber:
        print("Enter MoMo Pin")
        pin = input("")
        if pin != MP:
            print("Invalid Pin. Exiting.")
            exit()
        clear_screen()

if userInput == "2":
    print("Sign Up for MoMo")
    print("Enter MoMo Number")
    userInput = input("")
    print("Set MoMo Pin")
    pin = input("")
    if len(pin) != 4 or not pin.isdigit():
        print("Pin must be a 4-digit number. Exiting.")
        exit()
    MP = pin
    save_data()
    clear_screen()
    print("MoMo Account Created Successfully!")
    input("Press Enter to continue...")
    clear_screen()


while True:
    clear_screen()
    momoMainmenu()

    userInput = input("")
    clear_screen()

    if userInput == "1":
        momoTransferMenu()
        userInput = input("")
        clear_screen()
        if userInput == "1":
            print("Enter Number")
            phoneNumber = input("")
            if not checkIfNumberIsAllowedMTN(phoneNumber):
                print("Invalid phone number.")
                input("Press Enter to continue...")
                clear_screen()
                continue
            clear_screen()

            print("Confirm Number")
            phoneNumber1 = input("")
            clear_screen()

            if phoneNumber in myContacts and phoneNumber == phoneNumber1:
                print("Enter Amount")
                amount = input("")
                clear_screen()

                print("Enter Reference")
                reference = input("")
                clear_screen()

                print(f"Transfer {amount} to {myContacts[phoneNumber]} with reference {reference}?")
                if verifyPin():
                    if momoWalletMenu(int(amount)):
                        th.append(f"Congratulations you have sent {amount} to {myContacts[phoneNumber]}")
                        save_data()  # SAVE AFTER TRANSACTION
                        print(th[-1])
                        input("Press Enter to continue...")
                        clear_screen()

            else:
                print("Add Phone Number To The COntact List First")                        

        elif userInput == "5":
            transferMoneyToOtherNetworksMenu()
            userInput = input("")
            clear_screen()
            if userInput == "1":
                print("Enter Number")
                phoneNumber = input("")
                if not checkIfNumberIsAllowedAT(phoneNumber):
                    print("Invalid phone number.")
                    input("Press Enter to continue...")
                    clear_screen()
                    continue
                clear_screen()

                print("Confirm Number")
                phoneNumber1 = input("")
                clear_screen()

                if phoneNumber in myContacts and phoneNumber == phoneNumber1:
                    print("Enter Amount")
                    amount = input("")
                    clear_screen()

                    print("Enter Reference")
                    reference = input("")
                    clear_screen()

                    print(f"Transfer {amount} to {myContacts[phoneNumber]} with reference {reference}?")
                    if verifyPin():
                        if momoWalletMenu(int(amount)):
                            print(f"Congratulations you have sent {amount} to {myContacts[phoneNumber]}")
                            input("Press Enter to continue...")
                            clear_screen()

            elif userInput == "2":
                    print("Enter Number")
            phoneNumber = input("")
            if not checkIfNumberIsAllowedTelecel(phoneNumber):
                    print("Invalid phone number.")
                    input("Press Enter to continue...")
                    clear_screen()
                    continue
            clear_screen()

            print("Confirm Number")
            phoneNumber1 = input("")
            clear_screen()

            if phoneNumber in myContacts and phoneNumber == phoneNumber1:
                    print("Enter Amount")
                    amount = input("")
                    clear_screen()

                    print("Enter Reference")
                    reference = input("")
                    clear_screen()

                    print(f"Transfer {amount} to {myContacts[phoneNumber]} with reference {reference}?")
                    if verifyPin():
                        if momoWalletMenu(int(amount)):
                            print(f"Congratulations you have sent {amount} to {myContacts[phoneNumber]}")
                            input("Press Enter to continue...")
                            clear_screen()


        elif userInput == "0":
                continue           
        
        else:
            print("Option not implemented yet.")
            break

                
    elif userInput == "2":
        momoPayMenu()

    elif userInput == "3":
        momoAirtimeBundlesMenu()

    elif userInput == "4":
        allowCashOutMenu()

    elif userInput == "5":
        financialMenu()
        userInput = input("")
        if userInput == "3":
            loansMenu()
            userInput = input("")
            clear_screen()
            if userInput in [str(i) for i in range(1, 8)]:
                loanMoney()
            else:
                print("Option not implemented yet.")
                break


    elif userInput == "6":
        myWalletMenu()
        userInput = input("")
        clear_screen()

        if userInput == "1":
            print("Fee is Ghs 0.00. Enter MM PIN")
            if verifyPin():
                print(f"Current Balance: Ghs {MomoAmount}, Available Balance: {MomoAmount}")
                input("Press Enter to continue...")
                clear_screen()

        elif userInput == "6":
            changePin()

        else:
            print("Option not implemented yet.")
            break

    elif userInput == "7":
        just4UMenu()

    elif userInput == "8":
        MomoAppMenu()

    elif userInput == "0":
        print("Thank you for using MoMo services")
        break

    elif userInput == "99":
        print("Transaction History")
        print(th)
        input("Press Enter to continue...")


    elif userInput == "#":
        addContact()

    else:
        print("Invalid option selected. Please try again.")

# END OF PROGRAM
#By Roland Yeboah (Rolie-CODE)
