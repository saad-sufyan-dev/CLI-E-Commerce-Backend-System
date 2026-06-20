class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        
    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, new_quantity):   
        if (new_quantity) <= self.product.stock and new_quantity>0:
            self.__quantity = new_quantity
        elif new_quantity == 0:
            self.__quantity = 0
        else:
            raise ValueError("Invalid quantity, not available in stock")

    def increase_quantity(self, quantity):
        if quantity>0:
            self.quantity += quantity
        else:
            raise ValueError("Quantity should be positive")

    def decrease_quantity(self, quantity):        
        if quantity>self.__quantity:
            raise ValueError("Can't remove more items than are currently in the cart")
        elif quantity>0:
            self.quantity -= quantity
        else:
            raise ValueError("Quantity should be positive")

    def get_total_price(self):
        return self.product.price * self.quantity
    
        
    def cartitem_info(self):
        details = [
            "",
            f"Name: {self.product.name}",
            f"Price: {self.product.price:,} Rs",
            f"Quantity: {self.quantity}",
            f"Net Price: {self.get_total_price():,} Rs"
        ]
        return "\n".join(details)
