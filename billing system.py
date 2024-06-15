import datetime

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Customer:
    def __init__(self, name='', address='', phone_number=''):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.cart = []

    def add_to_cart(self, product, quantity):
        self.cart.append((product, quantity))

    def remove_from_cart(self, product_name):
        self.cart = [(product, quantity) for product, quantity in self.cart if product.name != product_name]

    def calculate_total(self):
        return sum(item.price * quantity for item, quantity in self.cart)

    def apply_discount(self, total, discount_rate):
        return total * (1 - discount_rate)

    def print_receipt(self, payment_type, cash_given=0, is_new=False):
        total = self.calculate_total()
        discount_rate = 0.05 if is_new else 0
        total_after_discount = self.apply_discount(total, discount_rate)
        return_amount = cash_given - total_after_discount if payment_type == 'cash' else 0

        print("\n------ Receipt ------")
        print(f"Market Name: {market.name}")
        print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d')}")
        print(f"Time: {datetime.datetime.now().strftime('%H:%M:%S')}")
        print("\n{:<20} {:<10} {:<15}".format("Product", "Quantity", "Total Price"))
        
        for item, quantity in self.cart:
            total_price_for_item = item.price * quantity
            print(f"{item.name:<20} {quantity:<10} {total_price_for_item:<15.2f}")
        
        print(f"\nTotal: {total:<15.2f}")
        if is_new:
            print(f"Discounted Total: {total_after_discount:<10.2f}")
        print(f"Payment Type: {payment_type}")
        if payment_type == 'cash':
            print(f"Cash Given: {cash_given:<15.2f}")
            print(f"Return Amount: {return_amount:<15.2f}")
        print("--------------------\n")

class RegularCustomer(Customer):
    def __init__(self, name='', address='', phone_number=''):
        super().__init__(name, address, phone_number)

class NewCustomer(Customer):
    def __init__(self, name='', address='', phone_number=''):
        super().__init__(name, address, phone_number)

class Market:
    def __init__(self):
        self.name = input("Please enter your market name: ")
        print(f"\nWelcome to {self.name} market!\n")
        self.products = []
        self.setup_products()

    def setup_products(self):
        num_of_products = int(input("How many products do you have in your market? "))
        for _ in range(num_of_products):
            name = input("Enter product name: ")
            price = float(input(f"Enter {name}'s price: "))
            self.add_product(Product(name, price))

    def add_product(self, product):
        self.products.append(product)

    def find_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product
        return None

    def display_menu(self):
        print("\nPlease choose an action:")
        print("  [add] - Add a product to the cart")
        print("  [remove] - Remove a product from the cart")
        print("  [total] - Display the current total")
        print("  [print] - Print the bill and proceed to payment")
        print("  [quit] - Exit without printing the bill")

    def start_billing_process(self):
        is_new = input("Are you a new customer? (yes or no): ").strip().lower() == 'yes'
        if is_new:
            customer = NewCustomer()
            customer.name = input("Please, enter your name: ")
            customer.address = input("Please, enter your address: ")
            customer.phone_number = input("Please, enter your phone number: ")
        else:
            customer = RegularCustomer()

        while True:
            self.display_menu()
            action = input("What would you like to do? ").strip().lower()
            if action == 'print':
                break
            elif action == 'add':
                product_name = input("Enter the name of product: ").strip()
                product = self.find_product(product_name)
                if product:
                    quantity = int(input("Enter quantity: "))
                    customer.add_to_cart(product, quantity)
                else:
                    print("Product not found.")
            elif action == 'remove':
                product_name = input("Enter the name of product to remove: ").strip()
                customer.remove_from_cart(product_name)
                print(f"{product_name} has been removed from the cart.")
            elif action == 'total':
                print(f"Current total: {customer.calculate_total():.2f}")
            elif action == 'quit':
                print("Exiting without printing the bill.")
                return
            else:
                print("Invalid action. Please try again.")

        payment_type = input("Enter payment type (cash/credit): ").strip().lower()
        cash_given = 0
        if payment_type == 'cash':
            cash_given = float(input("Enter the amount of cash given: "))
        customer.print_receipt(payment_type, cash_given, is_new=is_new)

market = Market()  
market.start_billing_process()
