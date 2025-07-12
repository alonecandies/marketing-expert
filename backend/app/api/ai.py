from fastapi import APIRouter, Depends, HTTPException
from app.services.deps import get_current_user
from app.services.conversation_service import ConversationService
from app.services.ai_service import generate_marketing_response

router = APIRouter(prefix="/ai", tags=["ai"])

@router.post("/chat/{conversation_id}")
def chat(conversation_id: str, current_user=Depends(get_current_user)):
    conv = ConversationService.get_conversation(conversation_id)
    if not conv or conv["user_id"] != current_user.id:
        raise HTTPException(status_code=404, detail="Conversation not found")
    messages = conv["messages"]
    ai_response = generate_marketing_response(messages)
    ConversationService.add_message(conversation_id, "assistant", ai_response)
    return {"response": ai_response}
