# Transaction model
class Transaction:

    def __init__(self, category, amount, description):
        self.category = category
        self.amount = amount
        self.description = description