from sqlalchemy.orm import Session
from .models import UserModel
from app.domain.user import User
from app.services.auth_service import get_password_hash, verify_password

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str):
        return self.db.query(UserModel).filter(UserModel.email == email).first()

    def get_by_id(self, user_id: int):
        return self.db.query(UserModel).filter(UserModel.id == user_id).first()

    def create(self, email: str, password: str):
        hashed_password = get_password_hash(password)
        user = UserModel(email=email, hashed_password=hashed_password)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def verify_user(self, email: str, password: str):
        user = self.get_by_email(email)
        if user and verify_password(password, user.hashed_password):
            return user
        return None

    def add_credits(self, user_id: int, amount: int):
        user = self.get_by_id(user_id)
        if user:
            user.credits += amount
            self.db.commit()
            self.db.refresh(user)
            return user
        return None
