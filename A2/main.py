# expenseTracker
import os 
from datetime import datetime

class Transaction:
    def __init__(self, type_str, category, amount, date_time=None):
        self.type_str = type_str
        self.category = category
        self.amonunt = float(amount)
        
        if date_time is None:
            self.date_time = datetime.now().strftime("%Y-%m-%d")
        else:
            self.date_time = date_time
    
    def to_text(self):
        return f"{self.type_str}|{self.category}|{self.amount}|{self.date_time}"
        
    
    