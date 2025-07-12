from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Message:
    role: str  # 'user' or 'assistant'
    content: str
    timestamp: str

@dataclass
class Conversation:
    id: str
    user_id: int
    messages: List[Message]
    created_at: str
    updated_at: str
