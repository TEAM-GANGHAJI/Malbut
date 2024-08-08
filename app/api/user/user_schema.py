from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional

class UserBase(BaseModel):
    username: str = Field(
        ...,
        description="사용자의 이름",
        example="홍길동"
    )
    # phone: str = Field(
    #     ...,
    #     description="사용자의 전화번호",
    #     example="010-1234-5678"
    # )
    # email: EmailStr = Field(
    #     ...,
    #     description="사용자의 이메일 주소",
    #     example="user@example.com"
    # )
    user_type: str = Field(
        ...,
        description="사용자의 유형 (예: 관리자, 일반 사용자 등)",
        example="일반 사용자"
    )

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    username: Optional[str] = Field(
        None,
        description="업데이트할 사용자의 이름",
        example="김철수"
    )
    phone: Optional[str] = Field(
        None,
        description="업데이트할 사용자의 전화번호",
        example="010-9876-5432"
    )
    user_type: Optional[str] = Field(
        None,
        description="업데이트할 사용자의 유형",
        example="관리자"
    )

class UserDelete(BaseModel):
    id: int = Field(
        ...,
        description="삭제할 사용자의 고유 ID",
        example=1
    )

class User(UserBase):
    id: int = Field(
        ...,
        description="사용자의 고유 ID",
        example=1
    )
    created_at: datetime = Field(
        ...,
        description="사용자 계정 생성 일시",
        example="2023-08-06T12:00:00"
    )

    class Config:
        from_attributes = True


# 추가적인 예시: 사용자 목록을 반환하는 응답 모델
# class UserList(BaseModel):
#     users: List[User] = Field(
#         ...,
#         description="사용자 목록",
#         example=[
#             {
#                 "id": 1,
#                 "username": "홍길동",
#                 "phone": "010-1234-5678",
#                 "user_type": "일반 사용자",
#                 "created_at": "2023-08-06T12:00:00"
#             },
#             {
#                 "id": 2,
#                 "username": "김철수",
#                 "phone": "010-9876-5432",
#                 "user_type": "관리자",
#                 "created_at": "2023-08-07T09:30:00"
#             }
#         ]
#     )
#     total: int = Field(
#         ...,
#         description="전체 사용자 수",
#         example=2
#     )