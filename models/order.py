from models.cart_item import CartItem
from models.customer import Customer
from copy import deepcopy
from textwrap import dedent

class Order:
    order_id_counter = 1000
    allowed_statuses = ["Pending", "Processing", "Shipped", "Delivered", "Canceled"]
    
    def __init__(self, customer: Customer):
        self.__customer = customer
        self.__items: list[CartItem] = deepcopy(customer.cart.cartitems)
        self.__total_amount = customer.cart.get_total()
        self.__order_id = Order.order_id_counter
        self.__order_status = "Pending"
        Order.order_id_counter+=1
            
    @property
    def customer(self):
        return self.__customer
        
    @property
    def items(self):
        return self.__items
    
    @property
    def total_amount(self):
        return self.__total_amount
    
    @property
    def order_id(self):
        return self.__order_id
    
    @property
    def order_status(self):
        return self.__order_status
    
    @order_status.setter
    def order_status(self, new_status):
        if new_status not in Order.allowed_statuses:
            raise ValueError(f"Order Status should match with:\n{Order.allowed_statuses}")
        self.__order_status = new_status
        
    def get_items_count(self):
        return len(self.items)

    def generate_invoice(self: Order):
        result = []
        for index, item in enumerate(self.items, start=1):
            result.append(f"\n[{index}] Product Details")
            result.append(item.cartitem_info().strip())
        
        intro_sec = dedent(f"""
        ========================================
                     ORDER INVOICE
        ========================================

        ----------------------------------------
                     CUSTOMER INFO
        ----------------------------------------
        Name   : {self.customer.name}
        Email  : {self.customer.email}
        ID     : {self.customer.customer_id}

        ----------------------------------------
                      ORDER INFO
        ----------------------------------------
        Order ID     : {self.order_id}
        Order Status : {self.order_status}
        Total Items  : {self.get_items_count()}

        ----------------------------------------
                        ITEMS
        ----------------------------------------""")
        
        items_sec = "\n".join(result)
        
        payment_sec = dedent(f"""
        ----------------------------------------
                    PAYMENT SUMMARY
        ----------------------------------------
        Final Paid Total: {self.total_amount:,} Rs

        ========================================
               THANK YOU FOR YOUR PURCHASE
        ========================================""")
        
        return f"{intro_sec}\n{items_sec}\n{payment_sec}"