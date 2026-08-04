from pydantic import BaseModel, EmailStr, Field, ConfigDict
from datetime import datetime

from app.models.enums import Role

class UserBase(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    email: EmailStr
    age: int = Field(ge=18, le=100)

class UserCreateRequest(UserBase):
    pass
    
class UserResponse(UserCreateRequest):
    id: int
    created_at: datetime
    role: Role
    model_config = ConfigDict(from_attributes=True)