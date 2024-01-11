from voucheritem import VoucherItem

class Voucher:
    def __init__(self, voucher_number, items=None):
        self.voucher_number = voucher_number
        self.items = items if items is not None else []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("Item not found in the voucher.")

    def update_item_amount(self, item, new_amount):
        if item in self.items:
            item.amount = new_amount
        else:
            print("Item not found in the voucher.")

    def calculate_total_amount(self):
        total_amount = sum(item.amount for item in self.items)
        return total_amount

    def display_voucher(self):
        print(f"Voucher Number: {self.voucher_number}")
        for item in self.items:
            print(item)
        print(f"Total Amount: Rs.{self.calculate_total_amount()}")
