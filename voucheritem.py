class VoucherItem:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount

    def __str__(self):
        return f"{self.description}: Rs.{self.amount}"
