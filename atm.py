from sys import *
print("Welcome To Kangal Bank ATM ")
restart = ("Y","Yes")
chances = 3
balance = 1000
while chances > 0:
    name = input("Enter Your Name :")
    pin = int(input("Enter Your Four Digit Password "))
    if pin == (1420):
        print("Hello ",name,",You Entered Your Pin Correctly")
        while restart not in ('n','NO','no','N'):
            print("Select Your Preferences \n")
            print("1. Balance Enquiry \n")
            print("2. Make a Withdrawl \n")
            print("3. To Deposit  \n")
            print("4. Return Card \n")
            options = int(input("Select Any One Option"))
            if options == 1:
                print("Your Current Balance is : RS ",balance)
                restart = input("Would You Like to Go Back, Yes/No : \n")
                if restart in ('No','N','n','no'):
                    print("Thank You For Banking With Us")
                    break
            elif options == 2:
                withdrawl = float(input("Enter the amount in the multiple of 100 to Withdraw : "))
                if (withdrawl > balance):
                    print("Insufficient Balance \n")
                elif withdrawl % 100 == 0:
                    balance = balance - withdrawl
                    print("Transaction Successfull, Your Updated Balance is",balance)
                    restart = input("Would You Like to Go Back, Yes/No : \n")
                    if restart in ('No','N','n','no'):
                        print("Thank You For Banking With Us")
                        break
            elif options == 3:
                deposit = float(input("How Much Do You Want To Deposit : \n"))
                balance = balance + deposit
                restart = input("Would You Like to Go Back, Yes/No : \n")
                printf("Amount Deposited Successfully, Your Updated Balance Is :",balance)
                if restart in ('No','N','n','no'):
                    print("Thank You For Banking With Us")
                    break
            elif options == 4:
                print("Please Wait While your Card is being returned : \n")
                print("Thank You For Your Service \n")
                break
            else:
                print("Choose Correct Option")
                restart = ('y')
    Amanelif pin != ('1420'):
            print("Incorrect Pin \n")
            chances = chances - 1
            if chances == 0:
                print("No More Tries \n")
                break
                    
                
            