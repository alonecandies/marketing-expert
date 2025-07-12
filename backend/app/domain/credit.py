from dataclasses import dataclass

@dataclass
class Credit:
    user_id: int
    amount: int
    description: str = ""
