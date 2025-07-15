

from pydantic import BaseModel

class CartsCreate(BaseModel):
    user_id:int
    product_id:int
    quantity:int
  

class CartsResponse(BaseModel):
    id: int
    user_id:int
    product_id:int
    quantity:int
  
class CartsUpdateRequest(BaseModel):
    quantity: int 
    product_id: int

    class Config:
        from_attributes = True


        

