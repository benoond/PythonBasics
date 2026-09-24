accounts={}
def AddAccount():
    while True:
        AccNum=input("Enter account number to add: ")
        new_Dict=dict()
        new_Dict["AccNum"]=AccNum
        accounts[AccNum]=new_Dict
        
        AccName=input("Enter customer's name: ")
        accounts[AccNum]["AccName"]=AccName
        
        AccBalance=input("Enter account balance: ")
        accounts[AccNum]["AccBalance"]=AccBalance
        print(accounts)
        while True:
            next=input("Do you want to add another accout Y/N: ")
            if next.lower()=="n":
                found = True
                break
            elif next.lower()=="y":
                continue
            else:
                print("Enter the correct option")
        if found:
            break

def ViewAccount():
    while True:
        AccNum=input("Enter account number to view or E to exit: ")
        if AccNum in accounts:
            print("Accout Detail")
            print("Name: ", accounts[AccNum]["AccName"], "Balance: ", accounts[AccNum]["AccBalance"])
        elif AccNum.lower()=="e":
            break
        else:
            print("Account Number do not exist")

#accounts = dict()

while True:
    print("1. Add Account")
    print("2. View Account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Delete Account")
    print("6. View All Accounts")
    print("7. Exit")

    choice=input("Enter the number of your option: ")

    if choice=="1":
        AddAccount()
    elif choice=="2":
        ViewAccount()
    elif choice=="3":
        Deposit()
    elif choice=="4":
        Withdraw()
    elif choice=="5":
        DeleteAccount()
    elif choice=="6":
        ViewAllAccount()
    else:
        print("Wrong Entry. Try again")

