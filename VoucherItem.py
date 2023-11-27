Muhammad Ibtsam Shakeel
S23BSEEN1E02047
class VoucherItem:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount

    def __str__(self):
        return f"{self.description}: Rs.{self.amount}"


class Voucher:
    def __init__(self, voucher_number, items=None):
        self.voucher_number = voucher_number
        self.items = items if items is not None else []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total_amount(self):
        total_amount = sum(item.amount for item in self.items)
        return total_amount

    def display_voucher(self):
        print(f"Voucher Number: {self.voucher_number}")
        for item in self.items:
            print(item)
        print(f"Total Amount: Rs.{self.calculate_total_amount()}")

# Creating Voucher Items
item1 = VoucherItem("Books", 5000)
item2 = VoucherItem("Laboratory Equipment", 10000)
item3 = VoucherItem("Software License", 5000)
item4 = VoucherItem("Tuition Fee", 20000)
item5 = VoucherItem("Library Fund", 5000)
item6 = VoucherItem("Electricity cost", 5000)
item7 = VoucherItem("Internet", 5000)
item8 = VoucherItem("Vehicle Points Fee", 7000)
item9 = VoucherItem("Others Funds", 5000)

# Creating a Voucher and Adding Items
voucher = Voucher(voucher_number="00001001")
voucher.add_item(item1)
voucher.add_item(item2)
voucher.add_item(item3)
voucher.add_item(item4)
voucher.add_item(item5)
voucher.add_item(item6)
voucher.add_item(item7)
voucher.add_item(item8)
voucher.add_item(item9)

# Displaying Voucher Information
voucher.display_voucher()
