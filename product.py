class Product:
    counter = 1000
    products = 0
    def __init__(self, name, price, stock):
        if price>0 and stock>=0:
            self.name = name
            self.price = price
            self.stock = stock
            self.product_id = Product.counter
            Product.counter+=1
            Product.products+=1

        else:
            raise ValueError("Invalid price or stock")

    @classmethod
    def get_total_products(cls):
        return cls.products

    def is_available(self, quantity):
        if quantity>0:
            return quantity<=self.stock
        else:
            raise ValueError("Invalid quantity")
    
    def reduce_stock(self, quantity):
        if self.is_available(quantity)==True:
            self.stock -= quantity
        else:
            raise ValueError("Invalid quantity")
            
    def restock(self, quantity):
        if quantity>0:
            self.stock += quantity
        else:
            raise ValueError("Invalid quantity")
        
    def update_price(self, new_price):
        if new_price>0:
            self.price = new_price
        else:
            raise ValueError("Invalid price")

    def get_details(self):
        details = [
            "",
            "Product Specifications:",
            f"Product Name:  {self.name}",
            f"Product Price: {self.price:,} Rs",
            f"Product Stock: {self.stock} pieces left",
            f"Product ID:    {self.product_id}"
        ]
        return "\n".join(details)