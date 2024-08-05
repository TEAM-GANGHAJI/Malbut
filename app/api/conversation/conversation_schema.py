from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional

class Message(BaseModel):
    role: str
    content: str

class Conversation(BaseModel):
    id: int
    messages: List[Message]

class ConversationResponse(BaseModel):
    conversation_id: int
    message: str

class ConversationRequest(BaseModel):
    message: str
    conversation_id: Optional[int] = None