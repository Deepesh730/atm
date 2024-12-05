class ATM:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.pin = "1234"  
        self.transaction_history = []

    def verify_pin(self):
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.pin:
            return True
        else:
            print("Incorrect PIN.")
            return False

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")
        self.transaction_history.append("Balance inquiry")

    def deposit_cash(self):
        amount = float(input("Enter the amount to deposit: "))
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ${amount}. New balance: ${self.balance}")
            self.transaction_history.append(f"Deposited ${amount}")
        else:
            print("Invalid amount. Please enter a positive amount.")

    def withdraw_cash(self):
        amount = float(input("Enter the amount to withdraw: "))
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Successfully withdrew ${amount}. New balance: ${self.balance}")
            self.transaction_history.append(f"Withdrew ${amount}")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            print("Invalid amount. Please enter a positive amount.")

    def change_pin(self):
        if self.verify_pin():
            new_pin = input("Enter new PIN: ")
            confirm_pin = input("Confirm new PIN: ")
            if new_pin == confirm_pin:
                self.pin = new_pin
                print("PIN successfully changed.")
                self.transaction_history.append("PIN changed")
            else:
                print("PINs do not match. PIN change unsuccessful.")

    def show_transaction_history(self):
        if self.transaction_history:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("No transactions yet.")

    def main_menu(self):
        while True:
            print("\nATM Main Menu:")
            print("1. Check Balance")
            print("2. Deposit Cash")
            print("3. Withdraw Cash")
            print("4. Change PIN")
            print("5. View Transaction History")
            print("6. Exit")

            choice = input("Choose an option (1-6): ")

            if choice == "1":
                if self.verify_pin():
                    self.check_balance()
            elif choice == "2":
                if self.verify_pin():
                    self.deposit_cash()
            elif choice == "3":
                if self.verify_pin():
                    self.withdraw_cash()
            elif choice == "4":
                self.change_pin()
            elif choice == "5":
                if self.verify_pin():
                    self.show_transaction_history()
            elif choice == "6":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")


atm = ATM(initial_balance=1000)  
atm.main_menu()
