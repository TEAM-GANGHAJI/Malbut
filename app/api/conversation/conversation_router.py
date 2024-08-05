from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from database.database import get_db
from api.conversation.conversation_schema import *
from api.conversation.conversation_crud import *
from typing import List
from common.logging import logger
from ..auth.auth_crud import get_current_user

router = APIRouter(
    prefix="/api/conversion",
    tags=["conversion"]
)

@router.post("/chat", response_model=ConversationResponse)
async def chat(
    request: ConversationRequest,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """
    사용자의 메시지를 받아 AI 교사의 응답을 반환합니다.
    """
    try:
        # 여기서 대화 기록을 데이터베이스에서 가져오거나 새로운 대화를 시작합니다.
        # 이 예시에서는 간단히 처리합니다.
        conversation_id = request.conversation_id or 0
        messages = [Message(role="user", content=request.message)]
        
        #ai_response = await get_ai_response(messages)
        ai_response = "GPT Response"
        # 대화 기록을 데이터베이스에 저장하는 로직을 여기에 구현합니다.
        
        return ConversationResponse(
            conversation_id=conversation_id + 1,
            message=ai_response
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"채팅 처리 중 오류 발생: {str(e)}")
    

@router.get("/conversations", response_model=List[Conversation])
async def get_conversations(
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """
    사용자의 모든 대화 기록을 반환합니다.
    """
    # 데이터베이스에서 사용자의 대화 기록을 가져오는 로직을 구현합니다.
    # 이 예시에서는 더미 데이터를 반환합니다.
    return [
        Conversation(
            id=1,
            messages=[
                Message(role="user", content="Hello"),
                Message(role="assistant", content="Hi there! How can I help you today?")
            ]
        )
    ]
