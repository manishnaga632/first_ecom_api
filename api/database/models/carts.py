from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from api.database.connection import Base

class Carts(Base):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False, index=True)
    quantity = Column(Integer)
    created_at = Column(DateTime, default=func.now())

    # # ✅ Relationships
    # user = relationship("User", back_populates="carts")  # Assuming the User class has a 'carts' relationship
    # product = relationship("Product", back_populates="carts")  # Assuming the Product class has a 'carts' relationship
    # reviews = relationship("Review", back_populates="product", cascade="all, delete-orphan")  # Assuming Review is related to Product
