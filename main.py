from manageaccount import createAccount


# Requirments.
# 1. ATM should be able to accept a card and ask for a pin.
# 2. ATM should be able to check if the pin is correct.
# 3. ATM should be able to check the balance of the card.
# 4. ATM should be able to withdraw money from the card.
# 5. ATM should be able to deposit money into the card.
# 6. ATM should be able to transfer money from one account to another.
# 7. ATM should be able to print the transaction history of the card.
# 8. ATM should be able to print the balance of the card.
# 9. ATM should be able to print the account details.




def main():
    print("Enter 0 to create a new account")
    print("Enter 1 to print account details")
    print("Enter 2 to check account balance")
    print("Enter 3 to withdraw money")
    print("Enter 4 to deposit money")
    print("Enter 5 to transfer money")
    print("Enter 6 to print transaction history")
    print("Enter 7 to create pin")
    print("Enter 8 to change pin ")
    print("Enter 9 to exit")

    choice = int(input("Enter your choice: "))
    if choice ==0:
        print("create a new account")
        createAccount()
    elif choice == 1:
        print("Account details")
        # print account details
    elif choice == 2:
        print("Account balance")
        # check account balance
    elif choice == 3:
        print("Withdraw money")
        # withdraw money
    elif choice == 4:
        print("Deposit money")
        # deposit money
    elif choice == 5:
        print("Transfer money")
        # transfer money
    elif choice == 6:
        print("Transaction history")
        # print transaction history
    elif choice ==7:
        print("Create pin")
        # print create pin
    elif choice ==8:
        print("Change pin")
        # change pin
    elif choice == 9:
        print("Exit")
        exit()
    else:
        print("Invalid choice")
        exit()


main()