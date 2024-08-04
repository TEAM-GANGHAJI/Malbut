from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database.database import get_db
from api.user.user_schema import UserCreate, UserUpdate, UserDelete, User
from api.user.user_crud import user_crud
from typing import List
from common.logging import logger

router = APIRouter()

@router.get("/", response_model=List[User])
async def get_user(db: AsyncSession = Depends(get_db)):
    logger.info(f"  [API] > USER: Get user")
    return await user_crud.get_all(db=db)


# @router.post("/token", response_model=Token)
# async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = authenticate_user(fake_users_db, form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user.username}, expires_delta=access_token_expires
#     )
#     return {"access_token": access_token, "token_type": "bearer"}


# @router.get("/users/me", response_model=User)
# async def read_users_me(current_user: User = Depends(get_current_user)):
#     return current_user


# @router.post("/logout")
# async def logout(current_user: User = Depends(get_current_user)):
#     # 실제 구현에서는 토큰을 블랙리스트에 추가하거나 Redis에서 제거하는 등의 작업을 수행해야 합니다
#     return {"message": "Successfully logged out"}


# @router.post("/kakao-login")
# async def kakao_login():
#     # 카카오 로그인 구현
#     # 실제 구현에서는 카카오 API를 사용하여 인증을 처리해야 합니다
#     return {"message": "Kakao login not implemented yet"}


# # 개인정보 수집 동의
# @router.post("/agree-privacy-policy")
# async def agree_privacy_policy(current_user: User = Depends(get_current_user)):
#     # 실제 구현에서는 사용자의 동의 여부를 데이터베이스에 저장해야 합니다
#     return {"message": "Privacy policy agreed"}