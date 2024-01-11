from voucheritem import VoucherItem
from voucher import Voucher

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
# ... (create more items if needed)

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

# ... (add more items if needed)

# Displaying Voucher Information
voucher.display_voucher()

# Additional Operations (Update, Remove)
voucher.update_item_amount(item1, 6000)
voucher.remove_item(item2)

# Displaying Updated Voucher Information
voucher.display_voucher()
