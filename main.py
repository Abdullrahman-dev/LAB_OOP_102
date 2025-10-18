from bank_account import BankAccount

def main():
    
    # Create a new Account :  
    
    account = BankAccount("Abdullrahman", 1000)

    print(f"👤 Account Holder: {account.get_account_holder()}")
    print(f"💰 Current Balance: {account.get_balance()} SR")

    
    try:
        new_balance = account.deposit(500)
        print(f"Deposited 500 SR. New balance: {new_balance} SR")
    except ValueError as e:
        print(e)

    try:
        new_balance = account.withdraw(300)
        print(f"Withdrawn 300 SR. New balance: {new_balance} SR")
    except Exception as e:
        print(e)

    try:
        account.withdraw(2000)
    except Exception as e:
        print(f"{e}")

    print(f"Final Balance: {account.get_balance()} SR")


if __name__ == "__main__":
    main()
