from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    email:str
    username:str
    password: str
    role: str

class UserResponse(BaseModel):
    id: int
    email: str
    username: str
    role: str

    class Config:
        from_attributes = True

class TicketCreate(BaseModel):
    title: str
    description: str
    priority: str

class TicketResponse(BaseModel):
    id: int
    title: str
    description: str
    priority: str
    status: str
    created_by: int
    assigned_to: int
    
    class Config:
        from_attributes = True

class TicketUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None

class CommentCreate(BaseModel):
    content:str

class CommentResponse(BaseModel):
    id : int
    content: str
    ticket_id: int
    user_id: int

    class Config:
        from_attributes = True