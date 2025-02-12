from fastapi import APIRouter, HTTPException
from models.chat_model import ChatRequest
from services.chat_service import generate_bot_reply

router = APIRouter()

@router.post("/chat")
async def chat(request: ChatRequest):
    if not request.message:
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    
    # ✅ Move business logic to a separate service
    bot_reply = generate_bot_reply(request.message)
    return {"reply": bot_reply}
