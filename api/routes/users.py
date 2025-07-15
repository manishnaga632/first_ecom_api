from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.database.schemas.user import UserResponse,UserPasswordUpdate,UserProfileUpdate
from api.token import get_current_user
from api.crud.user import update_user_password,get_user_by_email, update_user_profile
# Creating an API router instance for handling user-related routes
router = APIRouter()

@router.get("/profile", response_model=UserResponse)
def get_profile(current_user: UserResponse = Depends(get_current_user)):
    """
    Retrieve the profile of the currently authenticated user.

    Args:
        current_user (UserResponse): The authenticated user obtained via dependency injection.

    Returns:
        UserResponse: The details of the logged-in user.
    """
    return current_user







@router.put("/profile update/", response_model=dict)
def update(user_id: int, user_data: UserProfileUpdate, db: Session = Depends(get_db)):
    return update_user_profile(db, user_id, user_data)


@router.put("/users/update-password")
def update_password(
    email: str, 
    password_data: UserPasswordUpdate, 
    db: Session = Depends(get_db)
):
    """API endpoint to update a user's password."""
    user = get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if password_data.new_password != password_data.confirm_password:
        raise HTTPException(status_code=400, detail="New password and confirmation password do not match")

    # Update password directly
    update_user_password(db, user, password_data.new_password)
    
    return {"message": "Password updated successfully"}


