class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transaction = []

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")

        self._transaction.append(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transaction)

    @property
    def _transactions(self):
        return self._transaction

    @staticmethod
    def validate_transaction(account, amount_to_add):
        if account.balance + amount_to_add < 0:
            raise ValueError('sorry cannot go in debt!')

        account.add_transaction(amount_to_add)
        return f'New balance: {account.balance}'

    def __len__(self):
        return len(self._transaction)

    def __getitem__(self, index):
        return self._transaction[index]

    def __eq__(self, obj):
        return self.balance == obj.balance

    def __ne__(self, obj):
        return self.balance != obj.balance

    def __lt__(self, obj):
        return self.balance < obj.balance

    def __gt__(self, obj):
        return self.balance > obj.balance

    def __le__(self, obj):
        return self.balance < obj.balance

    def __ge__(self, obj):
        return self.balance >= obj.balance

    def __add__(self, obj):
        name = f'{self.owner}&{obj.owner}'
        starting_amount = self.amount + obj.amount

        new = Account(name, starting_amount)
        new._transaction = self._transaction + obj._transaction

        return new

    def __reversed__(self):
        return reversed(self._transaction)

    def __str__(self):
        return f'Account of {self.owner} with starting amount: {self.amount}'

    def __repr__(self):
        return f'Account({self.owner}, {self.amount})'