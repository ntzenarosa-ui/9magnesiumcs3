class BankAccount:

    def __init__(self, account_number, balance):
        # initialize attributes and validate initial balance
        self._account_number = account_number
        self.__balance = 0
        self.set_balance(balance)

    def set_account_number(self, account_number):
        # setter method to update or set the account number
        self._account_number = account_number

    @property
    def account_number(self):
        # getter method to securely access the account number through property decorator
        return self._account_number

    def set_balance(self, balance):
        # setter method for balance with validation against negative values
        if balance >= 0:
            self.__balance = balance
        else:
            print("The balance must be not a negative number.")

    @property
    def balance(self):
        # getter method to get the current balance
        return self.__balance

# testing
a1 = BankAccount(14163, 1430)
print("Account 1")
print(f"Account number: {a1.account_number}") # displays the account number of the first account
print(f"Balance: {a1.balance:.2f}") # displays the balance of the first account
print()
print("Update balance to -100")
a1.set_balance(-100) # updates the balance to -100
print(f"Account Number: {a1.account_number}") # displays the account number of the first account
print(f"Balance: {a1.balance:.2f}") # displays the balance of the first account