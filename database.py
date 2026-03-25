from sqlalchemy import create_engine, Column, Integer, String,
Float, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker,
declarative_base
import datetime
import matplotlib.pyplot as plt
# Initialize database
Base = declarative_base()
engine = create_engine('sqlite:///ecommerce.db')
Session = sessionmaker(bind=engine)
session = Session()
# Many-to-Many Association Table (Orders & Products)
order_product_table = Table(
'order_product', Base.metadata,
Column('order_id', Integer, ForeignKey('orders.order_id')),
Column('product_id', Integer,
ForeignKey('products.product_id')),
Column('quantity', Integer)
)
# Customer Model
class Customer(Base):
__tablename__ = 'customers'
customer_id = Column(Integer, primary_key=True)
name = Column(String)
email = Column(String)
created_at = Column(DateTime,
default=datetime.datetime.utcnow)
orders = relationship('Order', back_populates='customer')
# Order Model
class Order(Base):
__tablename__ = 'orders'
order_id = Column(Integer, primary_key=True)
customer_id = Column(Integer,
ForeignKey('customers.customer_id'))
order_date = Column(DateTime,
default=datetime.datetime.utcnow)
customer = relationship('Customer', back_populates='orders')
products = relationship('Product',
secondary=order_product_table, back_populates='orders')
# Product Model
class Product(Base):
__tablename__ = 'products'
CP465 – Database II Assignment #2 Page 6 of 9
product_id = Column(Integer, primary_key=True)
name = Column(String)
price = Column(Float)
orders = relationship('Order',
secondary=order_product_table, back_populates='products')
# Create database tables
Base.metadata.create_all(engine)