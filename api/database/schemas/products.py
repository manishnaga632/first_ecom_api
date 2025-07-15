from pydantic import BaseModel
from typing import Literal

# User creation schema
class ProductCreate(BaseModel):

    category_id : int 
    name : str 
    description : str 
    status: Literal["Active", "Inactive"]
    mrp : float
    net_price : float
    quantity_in_stock : int 
    image : str 
   
# Response model (excluding sensitive data)
class ProductResponse(BaseModel):

    id: int
    category_id : int 
    name : str 
    description : str 
    status: Literal["Active", "Inactive"]
    mrp : float
    net_price : float
    quantity_in_stock : int 
    image : str 
   

class ProductUpdate(BaseModel):

    category_id : int 
    name : str 
    description : str 
    mrp : float
    net_price : float
    quantity_in_stock : int 
    image : str 
   
    
    class Config:
        from_attributes = True
