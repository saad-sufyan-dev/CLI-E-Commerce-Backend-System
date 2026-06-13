from product import Product

class CartItem:
    cartitems = 0
    def __init__(self, product, quantity):
        self.product = product
        if quantity<=self.product.stock and quantity>0:
            self.quantity = quantity
            CartItem.cartitems+=1 
        else:
            raise ValueError("Invalid quantity, not available in stock")

    def get_total_price(self):
        return self.product.price, * self.quantity
    
    def increase_quantity(self, quantity):
        if quantity>0 and (self.quantity+quantity)<=self.product.stock:
            self.quantity+= quantity
        else:
            raise ValueError("Invalid quantity")
        
    def decrease_quantity(self, quantity):
        dif = self.quantity - quantity
        
        if dif > 0 and quantity>0:
            self.quantity -= quantity
        elif dif ==0:
            self.quantity=0
            return 0
        else:
            raise ValueError("Invalid quantity")
        
    def get_details(self):
        details = [
            "",
            f"Name: {self.product.name}",
            f"Price: {self.product.price:,} Rs",
            f"Quantity: {self.quantity}",
            f"Net Price: {self.get_total_price():,} Rs"
        ]
        return "\n".join(details)
