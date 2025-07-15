from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from api.database.connection import Base

class Categories(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    
    created_at = Column(DateTime, default=func.now())  
    updated_at = Column(DateTime, onupdate=func.now(), nullable=True)  # ✅ Automatically updates

    # # ✅ Relationship with Products
    # products = relationship("Products", back_populates="category", cascade="all, delete-orphan")
