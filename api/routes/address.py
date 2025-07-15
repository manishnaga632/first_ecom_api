from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.database.schemas.address import AddressCreate, AddressResponse, AddressUpdateRequest
from api.crud.address import create_address, update_address, delete_address, get_all_address
from typing import List

# Create a new API router for handling address-related endpoints
router = APIRouter()

@router.post("/add", response_model=AddressResponse)
def add(address: AddressCreate, db: Session = Depends(get_db)):
    return create_address(db, address)

@router.put("/update/{address_id}", response_model=AddressResponse)
def update_address_endpoint(address_id: int, address_data: AddressUpdateRequest, db: Session = Depends(get_db)):
    updated_address = update_address(db, address_id, address_data)
    if not updated_address:
        raise HTTPException(status_code=404, detail="Address not found")
    return updated_address

@router.delete("/delete/{address_id}", response_model=dict)
def delete(address_id: int, db: Session = Depends(get_db)):
    return delete_address(db, address_id)

@router.get("/all_address", response_model=List[AddressResponse])
def list_addresses(db: Session = Depends(get_db)):
    return get_all_address(db)
