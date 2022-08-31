# bank_account.py

class BankAccount:
    '''
    A class to be used to manage all registered bank accounts using a program.
    the currency is in dollars '$'
    '''
    
    currency = '$'

    def __init__(self, customer, account_number, balance=0):
        '''
        Method to initialize the attributes customer, account number, and balance
        '''
        
        self.customer = customer
        self.account_number = account_number
        self.balance = balance
        
    def deposit(self, amount):
        '''
        Method for depositing money to the bank account
        '''
        
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid deposit amount. Please try again.")
        
    def withdraw(self, amount):
        '''
        Method for withdrawing money from the bank account
        '''
        
        if amount > 0:
            if self.balance > amount:
                self.balance -= amount
            else:
                print("Insufficient funds!")
        else:
            print("Invalid withdraw amount. Please try again.")

    def check_balance(self):
        '''
        Method for checking the balance of an account
        '''
        
        print('The balance of account number {:d} is {:s}{:f}'.format(self.account_number, self.currency, self.balance))

