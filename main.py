from product import Product
from cart_item import CartItem
from cart import Cart
from customer import Customer

p1 = Product("Hp Laptop", 32000, 15)
p2 = Product("Dell Laptop", 26000, 10)
p3 = Product("Lenovo Laptop", 40000, 25)
p4 = Product("Macbook Air", 178000, 13)

c1 = Customer("Michael", "mca@hotmail.com")

print(p1.product_info())
print(p2.product_info())
print(p3.product_info())
print(p4.product_info())

c1.add_to_cart(p4, 1)
print(c1.view_cart())