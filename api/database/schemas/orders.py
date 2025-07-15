from pydantic import BaseModel
from typing import Optional

class OrdersCreate(BaseModel):
    user_id: int
    subtotal: int
    discount: float
    total: float
    status: str
    shipping_address: str

class OrdersResponse(BaseModel):
    id: int
    user_id: int
    subtotal: int
    discount: float
    total: float
    status: str
    shipping_address: str

class OrdersUpdateRequest(BaseModel):
    subtotal: Optional[int] = None
    discount: Optional[float] = None
    total: Optional[float] = None
    status: Optional[str] = None
    shipping_address: Optional[str] = None

    class Config:
        from_attributes = True
