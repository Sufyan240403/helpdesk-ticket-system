from database import engine, Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String,  index=True)
    email = Column(String, unique=True, index=True)
    created_at = Column(DateTime)
    password = Column(String, nullable=False)
    role = Column(String, default="user")

class Ticket(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    priority = Column(String, default="low")
    status = Column(String, default="open")
    created_by = Column(Integer, ForeignKey("users.id"))
    assigned_to = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    closed_at = Column(DateTime)

class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer, ForeignKey("tickets.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    content = Column(Text)
    created_at = Column(DateTime)

Base.metadata.create_all(bind=engine)
