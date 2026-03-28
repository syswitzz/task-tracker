from datetime import datetime
from pydantic import BaseModel, Field, EmailStr, ConfigDict


class UserCreate(BaseModel):
    username: str = Field(min_length=1, max_length=50)
    email: EmailStr = Field(max_length=100) # no min length req., as EmailStr already validates the email


class UserResponse(UserCreate):
    model_config = ConfigDict(from_attributes=True)  # allows us to create a UserResponse from a User model instance without manually converting it to a dict first
    
    id: int


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str | None = Field(default=None, max_length=200)
    completed: bool = False
    user_id: int


class TaskResponse(TaskCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    date_created: datetime
    author: UserResponse
    
