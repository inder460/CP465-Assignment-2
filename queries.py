# Retrieve all orders for a given customer
def get_customer_orders(customer_name):
customer =
session.query(Customer).filter_by(name=customer_name).first()
if customer:
print(f"\nOrders for {customer.name}:")
for order in customer.orders:
print(f"Order ID: {order.order_id}, Date:
{order.order_date}")
else:
print("Customer not found.")
get_customer_orders("Alice Johnson")
Retrieve all products in a specific order
def get_order_products(order_id):
order =
session.query(Order).filter_by(order_id=order_id).first()
if order:
print(f"\nProducts in Order {order_id}:")
for product in order.products:
print(f"{product.name} - ${product.price}")
else:
print("Order not found.")
get_order_products(1)
Calculate total revenue per customer
def get_total_spent_per_customer():
results = session.query(Customer, Order).join(Order).all()
customer_spending = {}
for customer, order in results:
total_spent = sum([product.price for product in
order.products])
if customer.name in customer_spending:
customer_spending[customer.name] += total_spent
else:
customer_spending[customer.name] = total_spent
print("\nTotal Revenue per Customer:")
for customer, total in customer_spending.items():
CP465 – Database II Assignment #2 Page 8 of 9
print(f"{customer}: ${total:.2f}")
return customer_spending
spending_data = get_total_spent_per_customer()