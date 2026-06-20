from cart_item import CartItem

class Cart:
    def __init__(self):
        self.cartitems = [] # --> will hold cartitems (obj of cartitem class)

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
        if len(self.cartitems)>0:
            print("\nCart Summary:")
            for index, item in enumerate(self.cartitems):
                print(f"\nItem # {index+1}:", end=" ")
                print(item.cartitem_info())

            print(f"\nTotal Payable Amount: {self.get_total():,} Rs")
        else:
            print("There are no items in your cart.")
