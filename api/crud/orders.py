from sqlalchemy.orm import Session
from api.database.models.orders import Orders
from api.database.schemas.orders import OrdersCreate,OrdersUpdateRequest
import pytz
from datetime import datetime, timedelta
from sqlalchemy import func

# Define IST timezone
IST = pytz.timezone("Asia/Kolkata")
def create_orders(db: Session, orders: OrdersCreate):

    db_orders = Orders(
        user_id=orders.user_id,
        subtotal=orders.subtotal,
        discount=orders.discount,
        total=orders.total,
        status=orders.status,
        shipping_address=orders.shipping_address,
       
       
    )
    db.add(db_orders)  # Add the user to the database session
    db.commit()  # Commit the transaction to save changes
    db.refresh(db_orders)  # Refresh the user instance with the latest data from DB
    return db_orders

# okk


def update_orders(db: Session, orders_id: int, orders_data: OrdersUpdateRequest):
    db_orders = db.query(Orders).filter(Orders.id == orders_id).first()
    
    if db_orders:
        # Update only if a new value is provided
        if orders_data.subtotal is not None:
            db_orders.subtotal = orders_data.subtotal
        if orders_data.discount is not None:
            db_orders.discount = orders_data.discount
        if orders_data.total is not None:
            db_orders.total = orders_data.total
        if orders_data.status is not None:
            db_orders.status = orders_data.status
        if orders_data.shipping_address is not None:
            db_orders.shipping_address = orders_data.shipping_address

        # ✅ Update `updated_at` to IST
        db_orders.updated_at = datetime.now(IST)

        db.commit()
        db.refresh(db_orders)
        return db_orders
    
    return None  # Order not found


def delete_orders(db: Session, orders_id: int):
     
    orders = db.query(Orders).filter(Orders.id == orders_id).first()
    if orders:
        db.delete(orders)
        db.commit()
        return {"success": True,"message": "orders deleted successfully"}
    
    return {"success": False,"message": "orders not found"}




def get_all_orders(db: Session):
    """
    Fetches all orders from the database.
    
    :param db: Database session.
    :return: A list of all orders.
    """
    return db.query(Orders).all()


def get_latest_orders(db: Session, limit: int = 5):
    return db.query(Orders).order_by(Orders.created_at.desc()).limit(limit).all()

def get_last_month_revenue(db: Session):
    last_month_start = datetime.now().replace(day=1) - timedelta(days=1)
    last_month_start = last_month_start.replace(day=1)
    last_month_end = last_month_start.replace(day=1) + timedelta(days=31)

    return db.query(func.sum(Orders.total)).filter(
        Orders.created_at >= last_month_start, Orders.created_at < last_month_end
    ).scalar() or 0

def get_last_three_months_revenue(db: Session):
    three_months_ago = datetime.now() - timedelta(days=90)
    return db.query(func.sum(Orders.total)).filter(Orders.created_at >= three_months_ago).scalar() or 0

def get_pending_orders(db: Session):
    return db.query(Orders).filter(Orders.status == "pending").all()

def get_all_delivered_orders(db: Session):
    return db.query(Orders).filter(Orders.status == "delivered").all()
