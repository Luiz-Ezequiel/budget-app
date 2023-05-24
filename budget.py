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
        if self.withdraw(amount, f'Transfer to {category.category}'):
            category.deposit(amount, f'Transfer from {self.category}')
            return True
        return False

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        return True
    
def create_spend_chart(categories):
    amount_spent = []
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item['amount'])
        amount_spent.append(round(spent, 2))

    total = round(sum(amount_spent), 2)
    percentage = list(map(lambda amount: int((((amount / total) * 10) // 1) * 10), amount_spent))

    header = "Percentage spent by category\n"

    chart = ""
    for value in reversed(range(0, 101, 10)):
        chart += str(value).rjust(3) + '|'
        for percent in percentage:
            if percent >= value:
                chart += ' o '
            else:
                chart += '   '
        chart += " \n"

    footer = "    " + "-" * ((3 * len(categories)) + 1) + "\n"
    descriptions = list(map(lambda category: category.category, categories))
    max_length = max(map(lambda description: len(description), descriptions))
    descriptions = list(map(lambda description: description.ljust(max_length), descriptions))
    for x in zip(*descriptions):
        footer += "    " + "".join(map(lambda s: s.center(3), x)) + " \n"

    return (header + chart + footer).rstrip("\n")

