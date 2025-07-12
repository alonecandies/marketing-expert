from pydantic import BaseModel, EmailStr

class UserCreateDTO(BaseModel):
    email: EmailStr
    password: str

class UserLoginDTO(BaseModel):
    email: EmailStr
    password: str

class UserDTO(BaseModel):
    id: int
    email: EmailStr
    credits: int

class TokenDTO(BaseModel):
    access_token: str
    token_type: str = "bearer"

class CreditTopUpDTO(BaseModel):
    amount: int
