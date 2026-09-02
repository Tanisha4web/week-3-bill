# Billing System - OOP Based

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total(self):
        return self.price * self.quantity


class Bill:
    def __init__(self):
        self.products = []
        self.tax_rate = 5  # 5% tax

    def add_product(self, product):
        self.products.append(product)

    def calculate_subtotal(self):
        total = 0

        for product in self.products:
            total += product.get_total()

        return total

    def calculate_tax(self):
        subtotal = self.calculate_subtotal()
        return subtotal * self.tax_rate / 100

    def calculate_total(self):
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()

        return subtotal + tax

    def display_bill(self):
        print("\n" + "=" * 60)
        print("                    FINAL BILL")
        print("=" * 60)

        print(f"{'Product':<20}{'Price':>10}{'Qty':>8}{'Total':>12}")
        print("-" * 60)

        for product in self.products:
            total = product.get_total()

            print(
                f"{product.name:<20}"
                f"₹{product.price:>9.2f}"
                f"{product.quantity:>8}"
                f"₹{total:>11.2f}"
            )

        print("-" * 60)

        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()
        total = self.calculate_total()

        print(f"{'Subtotal':<45}₹{subtotal:>11.2f}")
        print(f"{'Tax (5%)':<45}₹{tax:>11.2f}")
        print("=" * 60)
        print(f"{'FINAL TOTAL':<45}₹{total:>11.2f}")
        print("=" * 60)


# Main Program

bill = Bill()

print("===== BILLING SYSTEM =====")

while True:
    name = input("\nEnter product name (or 'done' to finish): ")

    if name.lower() == "done":
        break

    price = float(input("Enter product price: ₹"))
    quantity = int(input("Enter quantity: "))

    product = Product(name, price, quantity)

    bill.add_product(product)

    print("Product added successfully!")

# Display final bill
bill.display_bill()
