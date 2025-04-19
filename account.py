


class Account:
    def __init__(self):
        self.__pin=0
        self.__account_number=None
        self.__account_holder_name=None
        self.__balance=0


    def check_pin(self,pin):
        if(not (pin>1000 and pin<9999)):
            print("Invalid pin")
            return False
        return True

    def create_pin(self):
        pin =int(input("Enter a 4 digit pin: "))
        if not self.check_pin(pin):
            print("Invalid pin")
            return False
        else:
            self.__pin=pin
            print("pin sucessfully created")
            return True

    def change_pin(self):
        pin = int(input("Enter new pin"))
        if not self.check_pin(pin):
            print("pin not valid")
            return False
        else:
            self.__pin=pin
            print("pin sucessfully changed")
            return True
            
    def create_account_number(self, account_number):
        self.__account_number=account_number
        print("account number sucessfully generated")

    def define_account_holder_name(self):
        name=input("Enter the name")
        if(len(name)>100):
            print("name should contain atmost 100 characters")
            return False
        else:
            self.name=name
            print("name sucessfully assigned")
            return True

    def check_balance(self):
        pass

    def credit_amout(self):
        pass

    def debit_amout(self):
        pass

    def account_details(self):
        print("Account number :", self.__account_number)
        print("Account Holder name: ", self.__account_holder_name)
        print("Account balace: ", self.__balance)

