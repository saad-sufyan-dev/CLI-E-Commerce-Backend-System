from product import Product
from cart_item import CartItem
from cart import Cart
from customer import Customer
from order import Order

p1 = Product("Dell Mouse", 499, 25)
p2 = Product("HP Mouse", 899, 25)
p3 = Product("Dell Monitor", 24999, 15)
p4 = Product("HP Monitor", 34999, 15)
p5 = Product("Audionic Dual Speakers", 19999, 20)
p6 = Product("MI BT Mini Speaker", 3499, 30)
Products = [p1, p2, p3, p4, p5, p6]

list(map(lambda x: print(x.product_info()), Products))
c2 = Customer("Haroon Traders", "HT@yahoo.com")

c2.add_to_cart(p2,15)
c2.add_to_cart(p4, 15)
print(c2.customer_info())
print(c2.view_cart())

o1 = Order(c2)
o1.order_status = "Processing"
print(o1.order_status)
print(o1.generate_invoice())