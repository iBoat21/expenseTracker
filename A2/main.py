# expenseTracker 
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
    def __init__(self):
        self.transactions = []
        
    def add_transaction(self, type_str, category, amount, date_time=None):
        if amount <= 0:
            print("Error: Amount must be greater than 0!")
            return
        
        new_tx = Transaction(type_str, category, amount, date_time)
        self.transactions.append(new_tx)
        print(f"Recorded successfully: {type_str} ({category}) | Date: {new_tx.date_time} | Amount: {amount:,.2f}")


if __name__ == "__main__":
    tracker = ExpenseTracker()
    print("=== Testing Week 2: Add Transaction ===")
    tracker.add_transaction("Income", "Salary", 30000.0)
    tracker.add_transaction("Expense", "Food", 150.0)
    tracker.add_transaction("Expense", "Invalid Amount", -50.0)