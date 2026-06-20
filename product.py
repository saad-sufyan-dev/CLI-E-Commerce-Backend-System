class Product:
    productid = 1000
    products = 0
    def __init__(self, name, price, stock):
        self.price = price
        self.stock = stock
        self.name = name
        self.__product_id = Product.productid
        Product.productid+=1
        Product.products+=1

    @classmethod
    def get_total_products(cls):
        return cls.products
    
    @property
    def product_id(self):
        return self.__product_id
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, new_price):
        if new_price>0:
            self.__price = new_price
        else:
            raise ValueError("Price should be greater than 0")
        
    @property
    def stock(self):
        return self.__stock
    
    @stock.setter
    def stock(self, stock):
        if stock >=0:
            self.__stock = stock
        else:
            raise ValueError("Stock should be greater than or equal to 0")
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        if new_name.strip():
            self.__name = new_name
        else:
            raise ValueError("Product name can't be empty")
    
    def is_available(self, quantity):
        if quantity<=0:
            raise ValueError("Quantity should be positive")
        return quantity<=self.stock

    def reduce_stock(self, quantity):
        if self.is_available(quantity):
            self.stock -= quantity
        else:
            raise ValueError("Invalid quantity, not available in stock")
            
    def restock(self, quantity):
        if quantity>0:
            self.stock += quantity
        else:
            raise ValueError("Stock should be greater than 0")

    def product_info(self):
        details = [
            "",
            "Product Specifications:",
            f"Product Name:  {self.name}",
            f"Product Price: {self.price:,} Rs",
            f"Product Stock: {self.stock} pieces left",
            f"Product ID:    {self.product_id}"
        ]
        return "\n".join(details)