from product import Product
from cart_item import CartItem
from cart import Cart

p1 = Product("Hp Laptop", 32000, 15)
p2 = Product("Dell Laptop", 26000, 10)
p3 = Product("Lenovo Laptop", 40000, 25)
p4 = Product("Macbook Air", 178000, 13)

p1.update_price(56000)
print(f"Updated Price of {p1.name}: {p1.price} Rs")

# print(p1.is_available(4))
# p1.reduce_stock(4)
# print(f"Stock of {p1.name}: {p1.stock}")

# print("Total Products: ", Product.get_total_products())

# print(p1.get_details())
# print(p2.get_details())
# print(p3.get_details())
# print(p4.get_details())

i1 = CartItem(p3,6)
print(i1.get_details())

# cart = Cart()
# cart.add_item(p1, 1)
# cart.add_item(p1, 4)
# cart.add_item(p4, 1)

# cart.decrease_item(1000,3)

# cart.get_cart_details()

# print(p1.get_details())
# print(p2.get_details())
# print(p3.get_details())
# print(p4.get_details())
