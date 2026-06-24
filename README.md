# CLI E-Commerce Backend System (Python)

## 📌 Overview

This project is a command-line based e-commerce backend system built in Python.
It simulates a real shopping experience where users can browse products, add them to a cart, and complete checkout operations.

The project is designed for learning and portfolio purposes, focusing on core software engineering principles.

---

## 🎯 Objectives

* Practice Object-Oriented Programming (OOP)
* Understand class relationships (composition, aggregation)
* Implement real-world backend logic
* Learn file-based data persistence
* Build a structured and scalable Python project

---

## 🧠 Key Features

### Product Management

* Add new products
* View available products
* Manage product stock
* Update product pricing

### Cart System

* Add products to cart
* Remove products from cart
* Track quantity of items
* Calculate total price dynamically

### Checkout System

* Validate product stock
* Deduct inventory after purchase
* Generate order summary
* Clear cart after checkout

### Customer System

* Store customer information
* Link customer with cart
* Maintain basic purchase history

---

## 🏗️ Project Structure

```
cli-ecommerce-backend/
│
├── main.py
├── store.py
├── product.py
├── cart.py
├── cart_item.py
├── customer.py
├── order.py
│
├── data/
│   ├── products.txt
│   ├── customers.txt
│   ├── orders.txt
│
├── utils/
│   ├── file_handler.py
│
└── README.md
```

---

## 🔗 Core Class Design

* **Product** → Represents an item in the store
* **CartItem** → Represents a product with quantity
* **Cart** → Manages cart items and calculations
* **Customer** → Holds user data and cart
* **Order** → Represents a completed purchase
* **Store** → Controls products, customers, and checkout process

---

## 💡 Concepts Practiced

* Classes and Objects
* Inheritance (optional extension)
* Composition (Customer → Cart → CartItems)
* Aggregation (CartItem → Product)
* File Handling (read/write .txt data)
* Modular programming
* Basic system design thinking

---

## 🚀 Future Improvements

* Add JSON or database storage
* Add authentication system
* Add discount and coupon system
* Add order history tracking
* Convert into Flask/Django API version

---

## 👨‍💻 Author: Saad Sufyan

Python learning project built for mastering OOP and backend fundamentals.
