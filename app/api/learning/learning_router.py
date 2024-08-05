from fastapi import APIRouter, HTTPException, Depends, File, UploadFile, status
from sqlalchemy.ext.asyncio import AsyncSession
from database.database import get_db
from api.learning.learning_schema import *
from api.learning.learning_crud import learning_crud
from typing import List
from common.logging import logger
from ..auth.auth_crud import get_current_user
from fastapi.responses import FileResponse


router = APIRouter(
    prefix="/api/learning",
    tags=["learning"]
)

@router.post("", response_model=Learning)
async def create_learning(
    learning_create: LearningCreate,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """학습 생성"""
    try:
        new_learning = await learning_crud.create(db, obj_in=learning_create)
        return new_learning
    except Exception as e:
        logger.error(f"학습 생성 중 오류 발생: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="학습 생성 중 오류가 발생했습니다.")


@router.post("/correct", response_model=CorrectionResponse)
async def correct_text(
    request: CorrectionRequest,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """
    텍스트를 들어오면 정해진 기준에 따라 GPT 피드백을 제공합니다.
    """
    try:
        correction_result = ''
        # gpt_response = await get_gpt_correction(request.text)
        
        # # GPT 응답을 파싱하여 필요한 정보를 추출합니다.
        # # 이 부분은 GPT의 응답 형식에 따라 조정이 필요할 수 있습니다.
        # parsed_response = parse_gpt_response(gpt_response)
        
        # correction_result = CorrectionResponse(
        #     overall_score=parsed_response['overall_score'],
        #     correctness_alerts=parsed_response['correctness_alerts'],
        #     coherence_score=parsed_response['coherence_score'],
        #     clarity=parsed_response['clarity'],
        #     corrected_text=parsed_response['corrected_text'],
        #     explanation=parsed_response['explanation'],
        #     grammar_rule=parsed_response['grammar_rule']
        # )
        return correction_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"교정 처리 중 오류 발생: {str(e)}")


@router.post("/vocab", response_model=LearningResponse)
async def add_vocabulary(
    vocab: VocabItem,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """
    새로운 단어를 학습 목록에 추가합니다.
    """
    try:
        # 여기에 데이터베이스에 단어를 저장하는 로직을 구현합니다.
        return LearningResponse(success=True, message="Vocabulary added successfully")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"단어 추가 중 오류 발생: {str(e)}")


@router.post("/sentence", response_model=LearningResponse)
async def add_sentence(
    sentence: SentenceItem,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """
    새로운 문장을 학습 목록에 추가합니다.
    """
    try:
        # 여기에 데이터베이스에 문장을 저장하는 로직을 구현합니다.
        return LearningResponse(success=True, message="Sentence added successfully")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"문장 추가 중 오류 발생: {str(e)}")

#pip install python-mutipart
# @router.post("/pronunciation/record", response_model=LearningResponse)
# async def record_pronunciation(
#     file: UploadFile = File(...),
#     word_or_sentence: str = "",
#     db: AsyncSession = Depends(get_db),
#     current_user: dict = Depends(get_current_user)
# ):
#     """
#     사용자의 발음 녹음을 업로드하고 저장합니다.
#     """
#     try:
#         # 여기에 파일을 저장하고 데이터베이스에 기록하는 로직을 구현합니다.
#         return LearningResponse(success=True, message="Pronunciation recorded successfully")
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"발음 녹음 중 오류 발생: {str(e)}")


@router.get("/pronunciation/feedback/{record_id}", response_model=PronunciationFeedback)
async def get_pronunciation_feedback(
    record_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """
    특정 발음 녹음에 대한 피드백을 제공합니다.
    """
    try:
        # 여기에 AI 모델을 사용하여 발음 피드백을 생성하는 로직을 구현합니다.
        # 이 예시에서는 더미 데이터를 반환합니다.
        return PronunciationFeedback(accuracy=0.85, feedback="Good pronunciation. Pay attention to the 'th' sound.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"발음 피드백 생성 중 오류 발생: {str(e)}")


@router.get("/pronunciation/correct/{word_or_sentence}")
async def get_correct_pronunciation(
    word_or_sentence: str,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """
    단어나 문장의 정확한 발음 오디오 파일을 제공합니다.
    """
    try:
        # 여기에 텍스트를 음성으로 변환하는 로직을 구현합니다.
        # 이 예시에서는 더미 파일을 반환합니다.
        dummy_file_path = "path/to/dummy/audio/file.mp3"
        return FileResponse(dummy_file_path, media_type="audio/mpeg")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"정확한 발음 생성 중 오류 발생: {str(e)}")


@router.get("/progress", response_model=dict)
async def get_learning_progress(
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """
    사용자의 학습 진행 상황을 반환합니다.
    """
    try:
        # 여기에 사용자의 학습 진행 상황을 계산하는 로직을 구현합니다.
        # 이 예시에서는 더미 데이터를 반환합니다.
        return {
            "total_words": 100,
            "learned_words": 50,
            "total_sentences": 50,
            "practiced_sentences": 25,
            "pronunciation_accuracy": 0.75
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"학습 진행 상황 조회 중 오류 발생: {str(e)}")