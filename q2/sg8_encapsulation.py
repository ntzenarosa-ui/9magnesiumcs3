class BankAccount:
    #
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self.__balance = balance
    #
    def set_account_number(self, account_number):
        self._account_number = account_number
    def get_account_number(self):
        return self._account_number
    #
    def set_balance(self, balance):
        if balance > -1:
            self.__balance = balance
    def get_balance(self):
        return self.__balance
a1 = BankAccount(14163, 1430)
print("Account 1")
print(f"Account number: {a1._account_number}") #displays the account number of the first account
print(f"Balance: {a1.__balance}") #displays the balance of the first account
