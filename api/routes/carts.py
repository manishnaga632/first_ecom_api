from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.database.schemas.carts import CartsCreate, CartsResponse
from api.crud.carts import create_cart, update_cart,delete_cart,get_all_carts
from typing import List




# Create a new API router for handling authentication-related endpoints
router = APIRouter()


@router.post("/add" , response_model=CartsResponse)
def add(cart: CartsCreate, db: Session = Depends(get_db)):
 
    return create_cart(db,cart)





@router.put("/update/{cart_id}", response_model=CartsResponse)
def update_cart_endpoint(cart_id: int, cart: CartsCreate, db: Session = Depends(get_db)):
    # Check if the cart exists and update it, or raise a 404 error if not found
    updated_cart = update_cart(db, cart_id, cart)
    if not updated_cart:
        raise HTTPException(status_code=404, detail="Cart not found")
    return updated_cart


@router.delete("/delete/{cart_id}", response_model=dict)
def delete(cart_id: int, db: Session = Depends(get_db)):
    return delete_cart(db, cart_id)


@router.get("/all_carts", response_model=List[CartsResponse])
def list_carts(db: Session = Depends(get_db)):
    return get_all_carts(db)
