from product import Product
from cart_item import CartItem
from cart import Cart

class Customer:
    customer_id = 1000
    customers = 0
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cart = Cart()
        self.customer_id = Customer.customer_id
        Customer.customers+=1
        Customer.customer_id+=1

    def get_details(self):
        details = [
            "",
            f"Customer Name: {self.name}",
            f"Customer Email: {self.email}"
            f"Customer ID: {self.customer_id}"
        ]
        return "\n".join(details)
    
    def get_cart(self):
        return self.cart
    
    