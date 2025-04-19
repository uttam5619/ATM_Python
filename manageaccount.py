from account import Account
import random



def createAccount():
    act = Account()
    account_number=random.randint(100000000000, 999999999999)
    act.create_account_number(account_number)
    act.create_pin()
    act.define_account_holder_name()
    act.account_details()

