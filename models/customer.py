from cart import Cart
from textwrap import dedent

class Customer:
    customer_id_counter = 1000

    @staticmethod
    def verify_email(email):
        return '@' in email
    
    def __init__(self, name, email):
        self.__email = email
        self.__name: str = name
        self.__customer_id = Customer.customer_id_counter
        self.__cart = Cart()
        Customer.customer_id_counter+=1

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, new_email):
        if not self.verify_email(new_email):
            raise ValueError("Invalid email")
        self.__email = new_email
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name: str):
        if not new_name.strip() or len(new_name)>23:
            raise ValueError("Customer name cant be empty and must be under 23 word limit")
        self.__name = new_name
    
    @property
    def customer_id(self):
        return self.__customer_id
    
    @property
    def cart(self):
        return self.__cart
    
    def add_to_cart(self, product, quantity):
        self.cart.add_item(product, quantity)   

    def decrease_from_cart(self, product_id, quantity):
        self.cart.decrease_item(product_id, quantity)
        
    def remove_from_cart(self, product_id):
        self.cart.remove_item(product_id)

    def view_cart(self):
        return self.cart.cart_info()

    def cart_total(self):
        return f"Total Payable Amount: {self.cart.get_total():,} Rs"
    
    def clear_cart(self):
        self.cart.clear_cart()
        
    def order_history(self):
        pass
        
    def customer_info(self):
        return dedent(f"""
    ========================================
                CUSTOMER DETAILS            
    ========================================

    Name: {self.name} 
    Email: {self.email}
    ID: {self.customer_id}
    Total items in cart: {self.cart.get_total_cartitems()}

    ----------------------------------------
        """)