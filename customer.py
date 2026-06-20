from cart import Cart

class Customer:
    customerid = 1000
    customers = 0

    @staticmethod
    def verify_email(email):
        return '@' in email
    
    def __init__(self, name, email):
        self.email = email
        self.name = name
        self.__customer_id = Customer.customerid
        self.cart = Cart()
        Customer.customers+=1
        Customer.customerid+=1

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, new_email):
        if self.verify_email(new_email):
            self.__email = new_email
        else:
            raise ValueError("Invalid email")
    
    @property
    def customer_id(self):
        return self.__customer_id
    
    def add_to_cart(self, product, quantity):
        self.cart.add_item(product, quantity)   

    def remove_from_cart(self, product_id):
        self.cart.remove_item(product_id)

    def get_cart(self):
        return self.cart
    
    def view_cart(self):
        self.cart.cart_info()

    def cart_total(self):
        return f"Total Payable Amount: {self.cart.get_total():,} Rs"
    
    def clear_cart(self):
        self.cart.clear_cart()
        
    def customer_info(self):
        details = [
            "",
            f"Customer Name: {self.name}",
            f"Customer Email: {self.email}",
            f"Customer ID: {self.customer_id}",
            f"Total items in cart: {self.cart.get_total_cartitems()}"
        ]
        return "\n".join(details)
    