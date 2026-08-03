from pydantic import BaseModel, EmailStr, Field
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

class UserCreateRequest(BaseModel):
    name: str = Field(min_length=3)
    email: EmailStr
    age: int = Field(ge=18, le=60)

class UserUpdateRequest(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=3)
    email: EmailStr
    age: int = Field(ge=18, le=60)
    
class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    age: int