from pydantic import BaseModel

class ReviewsCreate(BaseModel):
    user_id: int
    order_id: int
    product_id: int
    rating: int
    review: str

class ReviewsResponse(BaseModel):
    id: int
    user_id: int
    order_id: int
    product_id: int
    rating: int
    review: str

    class Config:
        from_attributes = True
