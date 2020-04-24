class Account:
    def __init__(self, id: int, name: str, balance=0):
        self.id = id
        self.name = name
        self.balance = balance

    def credit(self, amount: int):
        self.balance += amount
        return self.balance

    def debit(self, amount: int):
        if self.balance < amount:
            return f'Amount exceeded balance'

        self.balance -= amount
        return self.balance

    def info(self):
        return f'User {self.name} with account {self.id} has {self.balance} balance'