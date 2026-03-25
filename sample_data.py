# Insert Customers
customer1 = Customer(name="Alice Johnson",
email="alice@example.com")
customer2 = Customer(name="Bob Smith", email="bob@example.com")
customer3 = Customer(name="Charlie Brown",
email="charlie@example.com")
session.add_all([customer1, customer2, customer3])
session.commit()
# Insert Products
product1 = Product(name="Laptop", price=1200.00)
product2 = Product(name="Smartphone", price=800.00)
product3 = Product(name="Headphones", price=150.00)
product4 = Product(name="Monitor", price=300.00)
product5 = Product(name="Keyboard", price=50.00)
session.add_all([product1, product2, product3, product4,
product5])
session.commit()
# Insert Orders
order1 = Order(customer_id=customer1.customer_id,
products=[product1, product3])
order2 = Order(customer_id=customer1.customer_id,
products=[product2, product5])
order3 = Order(customer_id=customer2.customer_id,
products=[product4])
order4 = Order(customer_id=customer3.customer_id,
products=[product2, product3, product5])
session.add_all([order1, order2, order3, order4])
session.commit()
