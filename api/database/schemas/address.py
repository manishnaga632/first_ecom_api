
from pydantic import BaseModel

class AddressCreate(BaseModel):
    user_id:int
    state: str
    city:str
    address_line1:str
    address_line2:str
    pincode:int
    complete_address:str
    

class AddressResponse(BaseModel):
    id: int
    user_id:int
    state: str
    city:str
    address_line1:str
    address_line2:str
    pincode:int
    complete_address:str
    
class AddressUpdateRequest(BaseModel):
    state: str
    city:str
    address_line1:str
    address_line2:str
    pincode:int
    complete_address:str
    

    class Config:
        from_attributes = True


