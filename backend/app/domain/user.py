from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    id: int
    email: str
    hashed_password: str
    credits: int = 0
