from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    mob_number: str
    role: str
    

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    password: str
    mob_number: str
    role: str

class UserProfileUpdate(BaseModel):

    name: str
    email: EmailStr
    mob_number: str
    role: str

    

    # Pydantic schema for password update
class UserPasswordUpdate(BaseModel):
 
    new_password: str
    confirm_password: str
  

    class Config:
        from_attributes = True
    

class UserLogin(BaseModel):
    email: str
    password: str
  

