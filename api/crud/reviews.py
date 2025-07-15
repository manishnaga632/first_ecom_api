
from sqlalchemy.orm import Session
from api.database.models.reviews import Reviews
from api.database.schemas.reviews import ReviewsCreate


def create_reviews(db: Session, reviews: ReviewsCreate):

    db_reviews = Reviews(
        user_id=reviews.user_id,
        order_id=reviews.order_id,
        product_id=reviews.product_id,
        rating=reviews.rating,
        review=reviews.review,
       
    )
    db.add(db_reviews)  # Add the user to the database session
    db.commit()  # Commit the transaction to save changes
    db.refresh(db_reviews)  # Refresh the user instance with the latest data from DB
    return db_reviews



def get_all_reviews(db: Session):
    """
    Fetches all reviews from the database.
    
    :param db: Database session.
    :return: A list of all reviews.
    """
    return db.query(Reviews).all()