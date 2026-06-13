from product import Product
from cart_item import CartItem

class Cart:
    def __init__(self):
        self.cartitems = [] # --> will hold cartitems (obj of cartitem class)

    def add_item(self, product, quantity):
        for i in self.cartitems:
            if i.product.product_id == product.product_id:
                if quantity>0 and (i.quantity+quantity)<=product.stock:
                    i.quantity +=quantity
                    break
                else:
                    raise ValueError("Invalid quantity, not available in stock")
        else:
            i = CartItem(product, quantity)
            self.cartitems.append(i)

    def get_total(self):
        t = 0
        for i in self.cartitems:
            v = i.get_total_price()
            t += v
        return t
    
    def get_total_cartitems(self):
        return len(self.cartitems)
    
    def get_cart_details(self):
        if len(self.cartitems)>0:
            print("\nCart Summary:")
            for index, item in enumerate(self.cartitems):
                print(f"\nItem # {index+1}:", end=" ")
                print(item.get_details())

            print(f"\nTotal Payable Amount: {self.get_total():,} Rs")
        else:
            print("There are no items in your cart.")

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
                result = i.decrease_quantity(quantity)
                if result == 0:
                    self.remove_item(product_id)
                    break
                else:
                    return None

        else:
            raise ValueError("A cartitem doesnt exist with that ID")          

    def clear_cart(self):
        self.cartitems.clear()
