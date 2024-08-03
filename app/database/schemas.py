from pydantic import BaseModel

class DbBase(BaseModel):
    id: int
    
    class Config:
        from_attributes = True  # Pydantic V2에서는 'orm_mode' 대신 'from_attributes'를 사용합니다.