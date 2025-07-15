from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, CheckConstraint, func
from api.database.connection import Base

class Reviews(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"), nullable=False, index=True)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False, index=True)
    rating = Column(Integer, CheckConstraint('rating >= 1 AND rating <= 5'), nullable=False)  # Rating must be between 1-5
    review = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
