import os 
from datetime import datetime

class Transaction:
    def __init__(self, type_str, category, amount, date_time=None):
        self.type_str = type_str
        self.category = category
        self.amount = float(amount)
        
        if date_time is None:
            self.date_time = datetime.now().strftime("%Y-%m-%d")
        else:
            self.date_time = date_time
    
    def to_text(self):
        return f"{self.type_str}|{self.category}|{self.amount}|{self.date_time}"

class ExpenseTracker:
    def __init__(self, file_name="expenseList.txt"):
        self.file_name = file_name
        self.transactions = []
        self.load_from_file()
        
    def add_transaction(self, type_str, category, amount, date_time=None):
        if amount <= 0:
            print("Error: Amount must be greater than 0!")
            return
        new_tx = Transaction(type_str, category, amount, date_time)
        self.transactions.append(new_tx)
        print(f"Recorded successfully: {type_str} ({category}) | Date: {new_tx.date_time} | Amount: {amount:,.2f}")
        self.save_to_file()
        
    def show_report(self):
        total_income = 0.0
        total_expense = 0.0
        print("\n--- Transaction History ---")
        if not self.transactions:
            print("No records found.")
        else:
            for idx, tx in enumerate(self.transactions, 1):
                print(f"{idx}. [{tx.type_str}] {tx.category:<15} | {tx.date_time} | {tx.amount:,.2f}")
                if tx.type_str == "Income":
                    total_income += tx.amount
                elif tx.type_str == "Expense":
                    total_expense += tx.amount

        balance = total_income - total_expense
        print("\n--- Summary Report ---")
        print(f"Total Income  : {total_income:,.2f}")
        print(f"Total Expense : {total_expense:,.2f}")
        print(f"Net Balance   : {balance:,.2f}\n")
        
    def save_to_file(self):
        with open(self.file_name, "w", encoding="utf-8") as file:
            for tx in self.transactions:
                file.write(tx.to_text() + "\n")
    
    def load_from_file(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        type_str, category, amount, date_time = line.split("|")
                        self.transactions.append(Transaction(type_str, category, float(amount), date_time))
            print(f"Loaded records from {self.file_name} successfully.")
        
if __name__ == "__main__":
    tracker = ExpenseTracker()
    while True:
        print("=== Main Menu ===")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Report")
        print("4. Exit")
        
        try:
            choice = int(input("Select an option (1-4): "))
        except ValueError:
            print("Invalid input: Please enter a number between 1 and 4.")
            continue
        
        match choice:
            case 1:
                cate = input("Enter income category: ")
                money = float(input("Enter amount: "))
                user_input_date = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
                tx_date = user_input_date if user_input_date else None
                tracker.add_transaction("Income", cate, money, date_time=tx_date)
            case 2:
                cate = input("Enter expense category: ")
                money = float(input("Enter amount: "))
                user_input_date = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
                tx_date = user_input_date if user_input_date else None
                tracker.add_transaction("Expense", cate, money, date_time=tx_date)
            case 3: 
                tracker.show_report()
            case 4:
                print("Exiting program. Goodbye!")
                break
            case _:
                print("Invalid option. Please try again.")