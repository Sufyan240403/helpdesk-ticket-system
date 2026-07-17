
from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from models import User
from schemas import UserCreate, UserResponse
from auth import create_access_token, hash_password, verify_password
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)
@router.post("/register")
def register (user: UserCreate, db:Session= Depends (get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=401, detail="invalid email or password")
    hashed_password = hash_password(user.password)
    new_user = User( username = user.username, email = user.email, password = hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "user created successfully"}


@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    result = verify_password(user.password, db_user.password)
    if not result:
        raise HTTPException(status_code=400, detail="Incorrect password")
    token = create_access_token(data={"sub": db_user.email})
    return {"token_type": "bearer","access_token": token} 
