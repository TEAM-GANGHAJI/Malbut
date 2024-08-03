from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database.database import get_db
from api.user.user_schema import UserCreate, UserUpdate, UserDelete, User
from api.user.user_crud import user_crud
from typing import List

import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/", response_model=List[User])
async def get_user(db: AsyncSession = Depends(get_db)):
    logger.info(f"[API] > USER: Get user")
    return await user_crud.get_all(db=db)
