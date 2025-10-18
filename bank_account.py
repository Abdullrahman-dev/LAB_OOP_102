class BankAccount:
    
    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.__account_holder = account_holder
        self.__balance = initial_balance

    def deposit(self, amount: float):
        
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount: float):
        
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.__balance:
            raise Exception("Insufficient funds.")
        self.__balance -= amount
        return self.__balance

    def get_balance(self):
        
        return self.__balance

    def get_account_holder(self):
        
        return self.__account_holder
