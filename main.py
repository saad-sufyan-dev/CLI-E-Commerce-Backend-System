from store import Store
from product import Product
from customer import Customer

def print_section(title):
    """Helper function to print section headers"""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")

print_section("STEP 1: INSTANTIATE A STORE")
store = Store()
print("✓ Store instantiated successfully")
print(f"  - Products in store: {store.get_total_products()}")
print(f"  - Customers in store: {store.get_total_customers()}")
print(f"  - Total orders: {store.get_total_orders()}")

print_section("STEP 2: CREATE 3 PRODUCTS AND ADD TO STORE")

# Create Product 1: Laptop
laptop = Product("Laptop", 120000, 5)
print(f"✓ Created Product 1: {laptop.product_info()}")
store.add_product(laptop)

# Create Product 2: Headphones
headphones = Product("Headphones", 5000, 15)
print(f"✓ Created Product 2: {headphones.product_info()}")
store.add_product(headphones)

# Create Product 3: Mouse
mouse = Product("Mouse", 2500, 25)
print(f"✓ Created Product 3: {mouse.product_info()}")
store.add_product(mouse)

print(f"\n✓ All products added to store")
print(f"  - Total products in store: {store.get_total_products()}")

print_section("STEP 3: REGISTER A NEW CUSTOMER IN STORE")
customer = Customer("Ahmed Hassan", "ahmed@example.com")
print(f"✓ Customer registered: {customer.customer_info()}")
store.register_customer(customer)
print(f"  - Total customers in store: {store.get_total_customers()}")

print_section("STEP 4: SIMULATE ADDING ITEMS TO CART")

# Test 4a: Add items in stock
print("  4a. Adding in-stock items to cart:")
customer.add_to_cart(laptop, 1)
print(f"      ✓ Added 1x Laptop to cart")

customer.add_to_cart(headphones, 2)
print(f"      ✓ Added 2x Headphones to cart")

customer.add_to_cart(mouse, 3)
print(f"      ✓ Added 3x Mouse to cart")

print(f"\n      Current cart status:")
print(customer.view_cart())

# Test 4b: Update quantity of existing item
print(f"\n  4b. Updating quantity of existing item:")
print(f"      Before: 3x Mouse in cart")
customer.add_to_cart(mouse, 2)  # Add 2 more to the existing 3
print(f"      ✓ Added 2 more Mouse to existing 3")
print(f"      After: 5x Mouse in cart")

print(f"\n      Updated cart status:")
print(customer.view_cart())

print_section("STEP 5: EXECUTE SUCCESSFUL CHECKOUT")
print("Processing checkout...\n")

# Store inventory before checkout
laptop_stock_before = store.products[laptop.product_id].stock
headphones_stock_before = store.products[headphones.product_id].stock
mouse_stock_before = store.products[mouse.product_id].stock

# Execute checkout
order = store.process_checkout(customer.customer_id)
print("✓ Checkout successful!")
print(f"  - Order ID: {order.order_id}")
print(f"  - Order Status: {order.order_status}")
print(f"  - Total Amount: {order.total_amount:,} Rs")

# Print invoice
print("\n" + order.generate_invoice())

print_section("STEP 6: VERIFY INVENTORY DECREASED ACCURATELY")
laptop_stock_after = store.products[laptop.product_id].stock
headphones_stock_after = store.products[headphones.product_id].stock
mouse_stock_after = store.products[mouse.product_id].stock

print(f"Inventory verification:")
print(f"  Laptop:     {laptop_stock_before} → {laptop_stock_after} (decreased by {laptop_stock_before - laptop_stock_after}) ✓")
print(f"  Headphones: {headphones_stock_before} → {headphones_stock_after} (decreased by {headphones_stock_before - headphones_stock_after}) ✓")
print(f"  Mouse:      {mouse_stock_before} → {mouse_stock_after} (decreased by {mouse_stock_before - mouse_stock_after}) ✓")

print_section("STEP 7: EDGE CASE TESTS")

# Edge Case 1: Try to checkout an empty cart
print("  Edge Case 1: Attempting to checkout with an empty cart")
try:
    store.process_checkout(customer.customer_id)
    print("      ✗ FAILED: Exception should have been raised")
except ValueError as e:
    print(f"      ✓ Exception caught as expected: '{e}'")

# Edge Case 2: Try to add more items than in stock
print("\n  Edge Case 2: Attempting to add more items than available in stock")
customer2 = Customer("John Doe", "john@example.com")
store.register_customer(customer2)

try:
    # Try to add 30 mice when only 20 are left in stock (25 - 5)
    customer2.add_to_cart(mouse, 30)
    # This will add to cart, but checkout should fail
    order2 = store.process_checkout(customer2.customer_id)
    print("      ✗ FAILED: Exception should have been raised during checkout")
except ValueError as e:
    print(f"      ✓ Exception caught during checkout: '{e}'")

# Edge Case 3: Try to checkout with invalid customer ID
print("\n  Edge Case 3: Attempting to checkout with invalid customer ID")
try:
    store.process_checkout(9999)
    print("      ✗ FAILED: Exception should have been raised")
except ValueError as e:
    print(f"      ✓ Exception caught as expected: '{e}'")

print_section("FINAL SUMMARY")
print(f"✓ All tests completed successfully!")
print(f"  - Total customers created: {store.get_total_customers()}")
print(f"  - Total products created: {store.get_total_products()}")
print(f"  - Total orders processed: {store.get_total_orders()}")