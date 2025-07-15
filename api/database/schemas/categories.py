from pydantic import BaseModel
from typing import Optional


class CategoryCreate(BaseModel):
    name: str
  

class CategoryResponse(BaseModel):
    id: int
    name: str
   

class CategoryUpdateRequest(BaseModel):
    name: Optional[str] = None
    

    class Config:
        from_attributes = True

