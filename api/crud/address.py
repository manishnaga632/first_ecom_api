from sqlalchemy.orm import Session
from api.database.models.address import Address
from api.database.schemas.address import AddressCreate, AddressUpdateRequest


# Create an Address
def create_address(db: Session, address: AddressCreate):
    db_address = Address(
        user_id=address.user_id,
        state=address.state,
        city=address.city,
        address_line1=address.address_line1,
        address_line2=address.address_line2,
        pincode=address.pincode,
        complete_address=address.complete_address,
    )
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address

# Update an existing Address
def update_address(db: Session, address_id: int, address_data: AddressUpdateRequest):
    db_address = db.query(Address).filter(Address.id == address_id).first()
    
    if db_address:
        # Update only if a new value is provided
        if address_data.state is not None:
            db_address.state = address_data.state
        if address_data.city is not None:
            db_address.city = address_data.city
        if address_data.address_line1 is not None:
            db_address.address_line1 = address_data.address_line1
        if address_data.address_line2 is not None:
            db_address.address_line2 = address_data.address_line2
        if address_data.pincode is not None:
            db_address.pincode = address_data.pincode
        if address_data.complete_address is not None:
            db_address.complete_address = address_data.complete_address

       

        db.commit()
        db.refresh(db_address)
        return db_address
    
    return None  # Address not found

# Delete an Address
def delete_address(db: Session, address_id: int):
    address = db.query(Address).filter(Address.id == address_id).first()
    if address:
        db.delete(address)
        db.commit()
        return {"success": True, "message": "Address deleted successfully"}
    
    return {"success": False, "message": "Address not found"}

# Get All Addresses
def get_all_address(db: Session):
    return db.query(Address).all()
