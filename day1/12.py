class BankAccount:
    def __init__(self, balance=0, pin=1111):
        self.balance = balance
        self.pin = pin

    def deposit(self, dep):
        self.balance += dep
        print(f"Amount: {dep} deposited successfully!")

    def withdraw(self, wth):
        if self.balance - wth < 0:
            print("Withdrawal not possible!")
            return
        self.balance -= wth
        print(f"Amount: {wth} withdrawn!")

    def get_balance(self):
        return self.balance
    
    def change_pin(self, pin):
        self.pin = pin
        print(f"PIN changed to {pin} successfully!")

class SavingsAccount(BankAccount):
    def __init__(self, balance=0, pin=1111, interest_rate=5):
        super().__init__(balance, pin)
        self.interest_rate = interest_rate

    def update_balance(self):
        self.balance += self.balance * (self.interest_rate / 100)
        print(f"Interest applied. New balance: {self.balance}")

class FreeSavingsAccount(SavingsAccount):
    def __init__(self, balance=0, pin=1111, interest_rate=5, charge=20):
        super().__init__(balance, pin, interest_rate)
        self.charge = charge

    def withdraw(self, wth):
        total_deduction = wth + self.charge
        if self.balance < total_deduction:
            print("Withdrawal not possible due to insufficient funds (including fees)!")
            return 
        self.balance -= total_deduction
        print(f"Amount: {wth} withdrawn. Fee: {self.charge} applied.")

user_bal = float(input("Enter initial balance: "))
user_pin = int(input("Set your 4-digit PIN: "))

account = FreeSavingsAccount(balance=user_bal, pin=user_pin)

while True:
    print("\n--- Bank Menu ---")
    print("1. Deposit")
    print("2. Withdraw (Note: 20 charge applies)")
    print("3. Check Balance")
    print("4. Apply Interest")
    print("5. Exit")
    
    choice = input("Select an option: ")

    if choice == '1':
        amt = float(input("Enter deposit amount: "))
        account.deposit(amt)
    elif choice == '2':
        amt = float(input("Enter withdrawal amount: "))
        account.withdraw(amt)
    elif choice == '3':
        print(f"Current Balance: {account.get_balance()}")
    elif choice == '4':
        account.update_balance()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")