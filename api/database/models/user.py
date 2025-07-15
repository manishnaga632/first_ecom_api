from sqlalchemy import Column, Integer, String,DateTime,func
from api.database.connection import Base
# from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    mob_number = Column(String(15), unique=True, nullable=False)
    role = Column(String(255), nullable=False)
    created_at=Column(DateTime,default=func.now())
    updated_at = Column(DateTime, default= func.now(),onupdate=func.now()) 

    # addresses = relationship("AAddress", back_populates="user", cascade="all, delete-orphan")
    # cart_items = relationship("Carts", back_populates="user", cascade="all, delete-orphan")
    # reviews = relationship("Reviews", back_populates="user", cascade="all, delete-orphan")
    # orders = relationship("Orders", back_populates="user", cascade="all, delete-orphan")
