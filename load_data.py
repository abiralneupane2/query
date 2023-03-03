import pandas as pd
from sqlalchemy.orm import Session

from schema import Order, Customer
from create_db import engine


if __name__=="__main__":
    orders_csv = pd.read_csv("olist_orders_dataset.csv")
    customers_csv = pd.read_csv("olist_customers_dataset.csv")

    orders = [Order(order_id, customer_id, order_purchase_timestamp, order_approved_at) \
        for order_id, customer_id, order_purchase_timestamp, order_approved_at in \
        zip(orders_csv["order_id"], orders_csv["customer_id"], orders_csv["order_purchase_timestamp"], orders_csv["order_approved_at"])]
    
    customers = [Customer(customer_id, customer_city, customer_state) \
        for customer_id, customer_city, customer_state in \
        zip(customers_csv["customer_id"], customers_csv["customer_city"], customers_csv["customer_state"])]

    with Session(engine) as session:
        session.bulk_save_objects(orders)
        session.bulk_save_objects(customers)
        session.commit()