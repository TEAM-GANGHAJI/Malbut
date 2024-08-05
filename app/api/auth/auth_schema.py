from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None
    ip: Optional[str] = None