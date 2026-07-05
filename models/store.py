from models.product import Product
from models.customer import Customer
from models.order import Order

class Store:
    def __init__(self):
        self.products: dict[int, Product] = {}
        self.customers: dict[int, Customer] = {}
        self.orders: list[Order] = []
        
    def add_product(self, product: Product):
        self.products[product.product_id] = product
        
    def register_customer(self, customer: Customer):
        self.customers[customer.customer_id] = customer
        
    def get_product(self, product_id: Product):
        if not self.products[product_id]:
            raise ValueError("There are no products in store that exist with that product_id")
        return self.products[product_id]
    
    def process_checkout(self, customer_id: int):
        c: Customer | None = self.customers.get(customer_id)
        if not c:
            raise ValueError("There are no customers in store that exist with that customer_id")
        elif len(c.cart.cartitems) == 0:
            raise ValueError("Cant checkout an empty cart")
        for i in c.cart.cartitems:
            if not i.quantity <= self.products[i.product.product_id].stock:
                raise ValueError(f"Invalid quantity of {i.product.name}, not available in stock")
        else:
            for i in c.cart.cartitems:
                self.products[i.product.product_id].stock -= i.quantity
            o = Order(c)
            self.orders.append(o)
            c.clear_cart()
            return o
        
    def get_total_orders(self):
        return len(self.orders)
        
    def get_total_customers(self):
        return len(self.customers)
    
    def get_total_products(self):
        return len(self.products)
    
    def product_catalog(self):
        if len(self.products) == 0:
            return "There are currently no products in the store"
        result = []
        result.append("\n" + "="*41)
        result.append("              PRODUCT CATALOG")
        result.append("="*41 + "\n")
        for index, product in enumerate(self.products.values(), start=1):
            result.append(f"[{index}] Product Details")
            result.append(product.product_info())
        return "\n".join(result)
        