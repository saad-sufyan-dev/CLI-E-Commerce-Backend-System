from cart_item import CartItem

class Cart:
    def __init__(self):
        self.cartitems: list[CartItem] = []
        
    def add_item(self, product, quantity):
        for i in self.cartitems:
            if i.product.product_id == product.product_id:
                i.increase_quantity(quantity)
                break
        else:
            i = CartItem(product, quantity)
            self.cartitems.append(i)

    def remove_item(self, product_id):
        for i in self.cartitems:
            if i.product.product_id == product_id:
                self.cartitems.remove(i)
                break
        else:
            raise ValueError("A cartitem doesnt exist with that ID")
        
    def decrease_item(self, product_id, quantity):
        for i in self.cartitems:
            if i.product.product_id == product_id:
                i.decrease_quantity(quantity)
                if i.quantity == 0:
                    self.remove_item(product_id)
                    break
                break
        else:
            raise ValueError("A cartitem doesnt exist with that ID")          

    def get_total(self):
        t = 0
        for i in self.cartitems:
            v = i.get_total_price()
            t += v
        return t
    
    def get_total_cartitems(self):
        return len(self.cartitems)
    
    def clear_cart(self):
        self.cartitems.clear()
    
    def cart_info(self):
        if not self.cartitems:
            return f"\nDear Customer, your shopping cart is currently empty."
        result = []
        result.append("\n" + "="*41)    
        result.append("              CART OVERVIEW")
        result.append("="*41)
        print
        for index, item in enumerate(self.cartitems, start=1):
            result.append(f"\n[{index}] Product Details")
            result.append(item.cartitem_info())
        result.append("\n" + "-"*41)
        result.append(f"Total Payable Amount: {self.get_total():,} Rs")
        result.append("-"*41)

        return "\n".join(result)