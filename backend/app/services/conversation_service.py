from app.infrastructure.mongo import conversations_collection
from app.domain.conversation import Conversation, Message
from datetime import datetime
from bson import ObjectId

class ConversationService:
    @staticmethod
    def create_conversation(user_id: int) -> str:
        now = datetime.utcnow().isoformat()
        conversation = {
            "user_id": user_id,
            "messages": [],
            "created_at": now,
            "updated_at": now
        }
        result = conversations_collection.insert_one(conversation)
        return str(result.inserted_id)

    @staticmethod
    def add_message(conversation_id: str, role: str, content: str):
        now = datetime.utcnow().isoformat()
        message = {
            "role": role,
            "content": content,
            "timestamp": now
        }
        conversations_collection.update_one(
            {"_id": ObjectId(conversation_id)},
            {"$push": {"messages": message}, "$set": {"updated_at": now}}
        )

    @staticmethod
    def get_conversation(conversation_id: str):
        conv = conversations_collection.find_one({"_id": ObjectId(conversation_id)})
        if not conv:
            return None
        return conv

    @staticmethod
    def get_user_conversations(user_id: int):
        return list(conversations_collection.find({"user_id": user_id}))
