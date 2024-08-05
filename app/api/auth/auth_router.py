
from fastapi import APIRouter, Depends, HTTPException, Response, Request
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from typing import Optional
# from jose import JWTError, jwt
from datetime import datetime, timedelta
from .auth_schema import Token, TokenData

# Auth 라우터
router = APIRouter(prefix="/auth", tags=["auth"])

@router.get("/token", response_model=Token)
async def token_test():
    access_token = 'access_token'
    return {"access_token": access_token, "token_type": "bearer"}
