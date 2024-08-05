from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database.database import get_db
from .user_schema import UserCreate, UserUpdate, UserDelete, User
from .user_crud import user_crud
from typing import List
from common.logging import logger
from ..auth.auth_crud import get_current_user

router = APIRouter(prefix="/users", tags=["user"])

@router.get("/", response_model=List[User])
async def get_user(db: AsyncSession = Depends(get_db)):
    logger.info(f"  [API] > USER: Get user")
    return await user_crud.get_all(db=db)


@router.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.post("/logout")
async def logout(current_user: User = Depends(get_current_user)):
    # 실제 구현에서는 토큰을 블랙리스트에 추가하거나 Redis에서 제거하는 등의 작업을 수행해야 합니다
    return {"message": "Successfully logged out"}


@router.post("/kakao-login")
async def kakao_login():
    # 카카오 로그인 구현
    # 실제 구현에서는 카카오 API를 사용하여 인증을 처리해야 합니다
    return {"message": "Kakao login not implemented yet"}


# 개인정보 수집 동의
@router.post("/agree-privacy-policy")
async def agree_privacy_policy(current_user: User = Depends(get_current_user)):
    # 실제 구현에서는 사용자의 동의 여부를 데이터베이스에 저장해야 합니다
    return {"message": "Privacy policy agreed"}