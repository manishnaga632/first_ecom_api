from sqlalchemy.orm import Session
from api.database.models.categories import Categories
from api.database.schemas.categories import CategoryCreate, CategoryUpdateRequest
from datetime import datetime
import pytz


# Define IST timezone
IST = pytz.timezone("Asia/Kolkata")


# Create a new category
def create_category(db: Session, category: CategoryCreate):
    db_category = Categories(
        name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

# Update an existing category
def update_category(db: Session, category_id: int, category_data: CategoryUpdateRequest):
    db_category = db.query(Categories).filter(Categories.id == category_id).first()
    
    if db_category:
        # Update only if a new value is provided
        if category_data.name is not None:
            db_category.name = category_data.name


 # Manually update `updated_at` to IST
        db_category.updated_at = datetime.now(IST)

        db.commit()
        db.refresh(db_category)
        return db_category
    
    return None  # Category not found

# Delete a category
def delete_category(db: Session, category_id: int):
    category = db.query(Categories).filter(Categories.id == category_id).first()
    
    if category:
        db.delete(category)
        db.commit()
        return {"success": True, "message": "Category deleted successfully"}
    
    return {"success": False, "message": "Category not found"}

# Fetch all categories
def get_all_categories(db: Session):
    return db.query(Categories).all()
