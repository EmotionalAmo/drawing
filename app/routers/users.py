from fastapi import APIRouter, Depends, HTTPException, status
from app.models.user_model import User, UserCreate, UserLogin
from sqlalchemy.orm import Session
from app.db.database import get_db
import hashlib


router = APIRouter()


@router.post("/register/", response_model=UserCreate)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = hashlib.sha256(user.password.encode()).hexdigest()
    query = User.insert().values(  # type: ignore
        email=user.email,
        username=user.username,
        password=hashed_password,
    )
    user_id = await db.execute(query)
    return {**user.model_dump(), "id": user_id}


@router.post("/login/")
async def login(user: UserLogin, db: Session = Depends(get_db)):
    query = User.select().where(User.username == user.username)  # type: ignore
    user_data = await db.fetch_one(query)  # type: ignore
    if user_data:
        stored_password = user_data["password"]
        hashed_password = hashlib.sha256(user.password.encode()).hexdigest()
        if stored_password == hashed_password:
            return {"message": "Login successful"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
    )


@router.post("/logout/")
async def logout():
    # Add your logout logic here
    return {"message": "Logout successful"}
