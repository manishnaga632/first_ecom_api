from sqlalchemy.orm import Session
from api.database.models.carts import Carts
from api.database.schemas.carts import CartsCreate,CartsUpdateRequest


def create_cart(db: Session, cart: CartsCreate):

    db_cart = Carts(
        user_id=cart.user_id,
        product_id=cart.product_id,
        quantity=cart.quantity,
       
    )
    db.add(db_cart)  # Add the user to the database session
    db.commit()  # Commit the transaction to save changes
    db.refresh(db_cart)  # Refresh the user instance with the latest data from DB
    return db_cart


def update_cart(db: Session, cart_id: int, cart_data: CartsUpdateRequest):
    # Query the database to find the cart by ID
    db_cart = db.query(Carts).filter(Carts.id == cart_id).first()
    
    if db_cart:
        # Update fields only if they are provided (None checks)
        if cart_data.quantity is not None:
            db_cart.quantity = cart_data.quantity
        if cart_data.product_id is not None:
            db_cart.product_id = cart_data.product_id

        db.commit()  # Commit the changes
        db.refresh(db_cart)  # Refresh the cart instance with updated data from DB
        return db_cart
    return None



# okk

def delete_cart(db: Session, cart_id: int):
     
    cart = db.query(Carts).filter(Carts.id == cart_id).first()
    if cart:
        db.delete(cart)
        db.commit()
        return {"success": True,"message": "cart deleted successfully"}
    
    return {"success": False,"message": "cart not found"}


def get_all_carts(db: Session):
    """
    Fetches all carts from the database.
    
    :param db: Database session.
    :return: A list of all carts.
    """
    return db.query(Carts).all()




