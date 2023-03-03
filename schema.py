from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

class Base(DeclarativeBase):
    pass



class Customer(Base):
    __tablename__ = "customers"
    customer_id = Column(String(30), primary_key=True)
    customer_city = Column(String)
    customer_state = Column(String)
    def __repr__(self) -> str:
        return f"Customer(id={self.id!r})"
    
    def __init__(self, customer_id, customer_city, customer_state):
        self.customer_id = customer_id
        self.customer_city = customer_city
        self.customer_state = customer_state

class Order(Base):
    __tablename__ = "orders"
    order_id = Column(String(30), primary_key=True)
    customer_id = Column(ForeignKey(Customer.customer_id))
    # order_status = Column(Integer)
    order_purchase_timestamp = Column(String)
    order_approved_at = Column(String)

    def __init__(self, order_id, customer_id, order_purchase_timestamp, order_approved_at):
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_purchase_timestamp = order_purchase_timestamp
        self.order_approved_at = order_approved_at

    def __repr__(self) -> str:
        return f"Order(id={self.order_id!r})"