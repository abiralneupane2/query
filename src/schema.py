from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase






class Base(DeclarativeBase):
    pass






class Customer(Base):
    """
    Schema for customers table
    """


    __tablename__ = "customers"
    customer_id = Column(String(30), primary_key=True)
    customer_city = Column(String)
    customer_state = Column(String)
    
    
    def __init__(self, customer_id, customer_city, customer_state):
        self.customer_id = customer_id
        self.customer_city = customer_city
        self.customer_state = customer_state


class Order(Base):
    """
    Schema for orders table
    """

    __tablename__ = "orders"
    order_id = Column(String(30), primary_key=True)
    customer_id = Column(ForeignKey(Customer.customer_id))
    order_purchase_timestamp = Column(String)
    order_approved_at = Column(String)

    def __init__(self, order_id, customer_id, order_purchase_timestamp, order_approved_at):
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_purchase_timestamp = order_purchase_timestamp
        self.order_approved_at = order_approved_at

    