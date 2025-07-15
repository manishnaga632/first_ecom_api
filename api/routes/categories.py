from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.database.schemas.categories import CategoryCreate, CategoryResponse, CategoryUpdateRequest
from api.crud.category import create_category, delete_category, get_all_categories, update_category
from typing import List

router = APIRouter()

# Add a category
@router.post("/add", response_model=CategoryResponse)
def add_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db, category)

# Update a category
@router.put("/update/{category_id}", response_model=CategoryResponse)
def update_category_endpoint(category_id: int, category_data: CategoryUpdateRequest, db: Session = Depends(get_db)):
    updated_category = update_category(db, category_id, category_data)
    if not updated_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return updated_category

# Delete a category
@router.delete("/delete/{category_id}", response_model=dict)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    return delete_category(db, category_id)

# List all categories
@router.get("/all", response_model=List[CategoryResponse])
def list_categories(db: Session = Depends(get_db)):
    return get_all_categories(db)
