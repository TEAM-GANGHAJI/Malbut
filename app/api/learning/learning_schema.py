from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class VocabItem(BaseModel):
    word: str
    meaning: str
    example_sentence: str

class SentenceItem(BaseModel):
    sentence: str
    translation: str

class PronunciationFeedback(BaseModel):
    accuracy: float
    feedback: str

class LearningResponse(BaseModel):
    success: bool
    message: str

class LearningCreate(BaseModel):
    pass

class LearningUpdate(BaseModel):
    pass

class LearningDelete(BaseModel):
    pass

class Learning(BaseModel):
    pass

# Pydantic Models
class CorrectionBase(BaseModel):
    original_text: str = Field(..., description="교정을 요청한 원본 텍스트")

class CorrectionCreate(CorrectionBase):
    pass

class CorrectionUpdate(BaseModel):
    corrected_text: Optional[str] = Field(None, description="교정된 텍스트")
    overall_score: Optional[int] = Field(None, ge=0, le=10, description="전체 점수 (0-10)")
    correctness_alerts: Optional[int] = Field(None, ge=0, description="정확성 경고 수")
    coherence_score: Optional[int] = Field(None, ge=0, le=10, description="일관성 점수 (0-10)")
    clarity: Optional[str] = Field(None, description="명확성 평가")
    explanation: Optional[str] = Field(None, description="교정에 대한 설명")
    grammar_rule: Optional[str] = Field(None, description="적용된 문법 규칙")

class CorrectionInDBBase(CorrectionBase):
    id: int
    user_id: int
    corrected_text: str
    overall_score: int
    correctness_alerts: int
    coherence_score: int
    clarity: str
    explanation: str
    grammar_rule: str
    created_at: datetime

    class Config:
        from_attributes = True

class Correction(CorrectionInDBBase):
    pass

class CorrectionInDB(CorrectionInDBBase):
    pass

# Request and Response Models
class CorrectionRequest(BaseModel):
    text: str = Field(..., description="교정을 요청할 텍스트")

class CorrectionResponse(BaseModel):
    original_text: str = Field(..., description="from database.base_class import Base원본 텍스트")
    corrected_text: str = Field(..., description="교정된 텍스트")
    overall_score: int = Field(..., ge=0, le=10, description="전체 점수 (0-10)")
    correctness_alerts: int = Field(..., ge=0, description="정확성 경고 수")
    coherence_score: int = Field(..., ge=0, le=10, description="일관성 점수 (0-10)")
    clarity: str = Field(..., description="명확성 평가")
    explanation: str = Field(..., description="교정에 대한 설명")
    grammar_rule: str = Field(..., description="적용된 문법 규칙")

# # 추가 모델 (필요에 따라 확장 가능)
# class CorrectionStatistics(BaseModel):
#     total_corrections: int
#     average_score: float
#     most_common_error: str