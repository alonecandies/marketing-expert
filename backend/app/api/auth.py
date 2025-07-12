from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.infrastructure.db import SessionLocal
from app.infrastructure.user_repository import UserRepository
from app.application.dto import UserCreateDTO, UserLoginDTO, UserDTO, TokenDTO, CreditTopUpDTO
from app.services.auth_service import create_access_token
from app.services.deps import get_current_user

router = APIRouter(prefix="/auth", tags=["auth"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup", response_model=UserDTO)
def signup(user_data: UserCreateDTO, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    if repo.get_by_email(user_data.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    user = repo.create(user_data.email, user_data.password)
    return UserDTO(id=user.id, email=user.email, credits=user.credits)

@router.post("/login", response_model=TokenDTO)
def login(user_data: UserLoginDTO, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    user = repo.verify_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": str(user.id)})
    return TokenDTO(access_token=token)

@router.post("/topup", response_model=UserDTO)
def topup(data: CreditTopUpDTO, current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    repo = UserRepository(db)
    user = repo.add_credits(current_user.id, data.amount)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserDTO(id=user.id, email=user.email, credits=user.credits)

@router.get("/me", response_model=UserDTO)
def get_me(current_user=Depends(get_current_user)):
    return UserDTO(id=current_user.id, email=current_user.email, credits=current_user.credits)
