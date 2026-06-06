# api/routes/chat.py
from fastapi import APIRouter, Request, HTTPException
from pydantic import BaseModel

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    user_id: str

@router.post("/chat")
async def chat_endpoint(payload: ChatRequest, request: Request):
    agent = getattr(request.app.state, "agent", None)
    if not agent:
        raise HTTPException(status_code=503, detail="Agent is not initialized")
    
    try:
        response_text = await agent.run(user_id=payload.user_id, user_input=payload.message)
        return {"response": response_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
