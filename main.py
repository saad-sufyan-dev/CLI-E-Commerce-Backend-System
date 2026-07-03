from models.cart import Cart
from models.customer import Customer
from models.order import Order
from models.product import Product
from models.store import Store

def main():
    # Phase 1: Product Testing
    laptop = Product("Laptop", 120000, 5)
    headphones = Product("Headphones", 5000, 15)
    mouse = Product("Mouse", 1500, 20)

    assert laptop.name == "Laptop"
    assert laptop.price == 120000
    assert laptop.stock == 5
    assert isinstance(laptop.product_id, int)
    assert "Laptop" in laptop.product_info()
    assert laptop.is_available(3) is True
    assert laptop.is_available(6) is False
    laptop.reduce_stock(1)
    assert laptop.stock == 4
    laptop.restock(1)
    assert laptop.stock == 5

    assert headphones.name == "Headphones"
    assert headphones.price == 5000
    assert headphones.stock == 15
    assert mouse.name == "Mouse"
    assert mouse.price == 1500
    assert mouse.stock == 20

    print("Product class methods verified.")

    # Phase 2: Cart & CartItem Testing
    customer = Customer("Ali Khan", "ali@example.com")
    assert customer.name == "Ali Khan"
    assert customer.email == "ali@example.com"
    assert isinstance(customer.customer_id, int)
    assert customer.cart.get_total_cartitems() == 0
    assert customer.cart_total() == "Total Payable Amount: 0 Rs"

    customer.add_to_cart(laptop, 2)
    customer.add_to_cart(headphones, 1)
    assert customer.cart.get_total_cartitems() == 2
    customer.add_to_cart(laptop, 1)
    assert customer.cart.cartitems[0].quantity == 3
    assert customer.cart.get_total_cartitems() == 2
    assert customer.cart.get_total() == (3 * laptop.price) + headphones.price
    assert customer.cart_total() == f"Total Payable Amount: {customer.cart.get_total():,} Rs"

    cart_item = customer.cart.cartitems[0]
    assert cart_item.quantity == 3
    assert cart_item.get_total_price() == 3 * laptop.price
    assert "Laptop" in cart_item.cartitem_info()
    cart_item.increase_quantity(1)
    assert cart_item.quantity == 4
    cart_item.decrease_quantity(1)
    assert cart_item.quantity == 3
    cart_item.quantity = 2
    assert cart_item.quantity == 2

    temp_cart = Cart()
    temp_cart.add_item(laptop, 1)
    temp_cart.add_item(headphones, 1)
    temp_cart.remove_item(headphones.product_id)
    assert temp_cart.get_total_cartitems() == 1
    temp_cart.add_item(headphones, 1)
    assert temp_cart.get_total_cartitems() == 2
    temp_cart.decrease_item(laptop.product_id, 1)
    assert temp_cart.get_total_cartitems() == 1
    assert temp_cart.get_total() == headphones.price
    temp_cart.clear_cart()
    assert temp_cart.get_total_cartitems() == 0
    assert "empty" in temp_cart.cart_info().lower()

    assert customer.view_cart().count("Laptop") >= 1
    customer.remove_from_cart(headphones.product_id)
    assert customer.cart.get_total_cartitems() == 1
    customer.add_to_cart(headphones, 1)
    customer.decrease_from_cart(laptop.product_id, 1)
    assert customer.cart.cartitems[0].quantity == 1
    assert customer.clear_cart() is None
    assert customer.cart.get_total_cartitems() == 0
    assert customer.order_history() is None
    assert "Ali Khan" in customer.customer_info()

    print("Cart and CartItem class methods verified.")

    # Phase 3: Store & Customer Registry Testing
    store = Store()
    store.add_product(laptop)
    store.add_product(headphones)
    store.add_product(mouse)
    store.register_customer(customer)
    assert store.products[laptop.product_id] is laptop
    assert store.products[headphones.product_id] is headphones
    assert store.products[mouse.product_id] is mouse
    assert store.customers[customer.customer_id] is customer
    assert store.get_total_products() == 3
    assert store.get_total_customers() == 1
    assert store.get_product(laptop.product_id) is laptop
    assert store.get_product(headphones.product_id) is headphones

    print("Store registration methods verified.")

    customer.add_to_cart(laptop, 2)
    customer.add_to_cart(headphones, 1)

    # Phase 4: Transaction & Order Lifecycle Testing
    order = store.process_checkout(customer.customer_id)
    assert isinstance(order, Order)
    assert store.products[laptop.product_id].stock == 3
    assert store.products[headphones.product_id].stock == 14
    assert customer.cart.get_total_cartitems() == 0
    assert store.get_total_orders() == 1
    assert order.customer is customer
    assert order.items[0].product.name == "Laptop"
    assert order.total_amount == 2 * laptop.price + headphones.price
    assert order.order_status == "Pending"
    assert order.get_items_count() == 2
    assert order.order_id >= 1000
    assert len(store.orders) == 1

    print("Transaction and Order methods verified.")
    print(order.generate_invoice())

    # Phase 5: Defensive Edge-Case Validation
    try:
        store.process_checkout(customer.customer_id)
        raise AssertionError("Checkout should have failed for an empty cart")
    except ValueError as error:
        assert "empty cart" in str(error).lower()

    print("Edge cases and validation safety verified.")


if __name__ == "__main__":
    main()
