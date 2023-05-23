class Category:
    def __init__(self, categories):
        self.category = categories
        self.ledger = []
        self.balance = 0.0

    def __repr__(self):
        title = self.category.center(30, "*") + '\n'
        ledger = ''
        for item in self.ledger:
            description = f"{item['description']:<23}"
            amount = f"{item['amount']:>7.2f}"
            ledger += f"{description[:23]}{amount[:7]}\n"
        total = f"Total: {self.balance:.2f}"
        return title + ledger + total
    
    def deposit(self, amount, description=''):
        self.balance += amount        
        self.ledger.append({'amount':amount,'description':description})
    
    def withdraw(self, amount, description=''):
        if self.balance - amount >= 0:
            self.ledger.append({'amount':amount*-1,'description':description})
            self.balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, category):
        if self.withdraw(amount, f'Transfer to {category}'):
            category.deposit(amount, f'Transfer to {category}')
            return True
        return False

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        return True
    
def create_spend_chart(categories):
    pass
