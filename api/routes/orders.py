from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.database.schemas.orders import OrdersCreate, OrdersResponse, OrdersUpdateRequest
from api.crud.orders import create_orders, update_orders, delete_orders, get_all_orders
from typing import List

# Create a new API router for handling order-related endpoints
router = APIRouter()

#  Create an Order
@router.post("/add", response_model=OrdersResponse)
def add_order(orders: OrdersCreate, db: Session = Depends(get_db)):
    return create_orders(db, orders)

#  Update an Order
@router.put("/update/{orders_id}", response_model=OrdersResponse)
def update_orders_endpoint(orders_id: int, orders_data: OrdersUpdateRequest, db: Session = Depends(get_db)):
    updated_order = update_orders(db, orders_id, orders_data)
    
    if not updated_order:  # Updated to check None instead of dictionary key
        raise HTTPException(status_code=404, detail="Order not found")
    
    return updated_order  # Returning the updated object directly

#  Delete an Order
@router.delete("/delete/{orders_id}", response_model=dict)
def delete_order(orders_id: int, db: Session = Depends(get_db)):
    result = delete_orders(db, orders_id)
    
    if not result["success"]:
        raise HTTPException(status_code=404, detail=result["message"])
    
    return result

#  Get All Orders
@router.get("/all_orders", response_model=List[OrdersResponse])
def list_orders(db: Session = Depends(get_db)):
    return get_all_orders(db)  # Returning list directly, no need for ["data"]
