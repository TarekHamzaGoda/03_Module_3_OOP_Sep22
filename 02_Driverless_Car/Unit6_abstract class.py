# Importing the abstract class module
from abc import ABC, abstractmethod


# creating the base class
class BankOperations(ABC):

    # creating abstract methods that will not be directly used
    @abstractmethod
    def current_balance(self):
        raise NotImplementedError()  # for calculating and viewing balance

    @abstractmethod
    def transfer_money(self):
        raise NotImplementedError  # to transfer money to another account

    @abstractmethod
    def deposit_money(self):
        raise NotImplementedError  # to add money in account


# Creating child class
class Banking(BankOperations):

    def __init__(self, my_balance=0):
        self.my_balance = my_balance

    # Class method to view current balance
    def current_balance(self):
        current_balance = self.my_balance
        print("Your current balance is =", current_balance)
        return

    # Class method to view calculate money transfer
    def transfer_money(self):
        send_amount = (int(input("Enter amount: ")))
        if self.my_balance <= send_amount:
            print("Not enough balance in account")
        else:
            new_balance = self.my_balance - send_amount
            self.my_balance = new_balance
            print("Amount Sent!. New balance is", new_balance)

    # Class method to view calculate money deposit
    def deposit_money(self):
        deposit_amount = (int(input("Enter deposit amount: ")))
        new_deposit_amount = deposit_amount + self.my_balance
        self.my_balance = new_deposit_amount
        print("Deposit completed, new balance is", {self.my_balance})


# Creating object with default balance of 1000
bank_operator = Banking(1000)


# Creating user menu interface
def bank_app():
    operation = int(input(""" Choose an operation:
    1. Current Balance
    2. Transfer Money
    3. Deposit Money
    4. Exit
    Your input: """))

    # object name is added as a parameter
    if operation == 1:
        Banking.current_balance(self=bank_operator)
        bank_app()

    elif operation == 2:
        Banking.transfer_money(self=bank_operator)
        bank_app()

    elif operation == 3:
        Banking.deposit_money(self=bank_operator)
        bank_app()

    elif operation == 4:
        print("Thank you!")
        exit()

    else:
        print("Wrong input!")


bank_app()

