from fastapi import APIRouter, Depends, HTTPException
from app.services.deps import get_current_user
from app.services.conversation_service import ConversationService

router = APIRouter(prefix="/conversations", tags=["conversations"])

@router.post("/start")
def start_conversation(current_user=Depends(get_current_user)):
    conv_id = ConversationService.create_conversation(current_user.id)
    return {"conversation_id": conv_id}

@router.post("/{conversation_id}/message")
def add_message(conversation_id: str, message: dict, current_user=Depends(get_current_user)):
    conv = ConversationService.get_conversation(conversation_id)
    if not conv or conv["user_id"] != current_user.id:
        raise HTTPException(status_code=404, detail="Conversation not found")
    ConversationService.add_message(conversation_id, message["role"], message["content"])
    return {"status": "ok"}

@router.get("/history")
def get_history(current_user=Depends(get_current_user)):
    conversations = ConversationService.get_user_conversations(current_user.id)
    return {"conversations": conversations}
