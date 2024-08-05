from fastapi.encoders import jsonable_encoder
from typing import Generic, TypeVar, List, Any, Dict, Union, Optional, List, Type
from sqlalchemy.orm import Session
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
#from schemas import UserModel, UserCreate, UserUpdate
from sqlalchemy.future import select
from sqlalchemy.sql.expression import BinaryExpression
import logging
from sqlalchemy.exc import SQLAlchemyError
from database.models import Base

logger = logging.getLogger(__name__)

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

#------------------------------------------------------------------------------------#
#                                      Class Crud                                                     
#------------------------------------------------------------------------------------#
class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    
    def __init__(self, model: Type[ModelType]):
        self.model = model
    
    async def get(
        self, db: AsyncSession, filter_condition: BinaryExpression
    ) -> ModelType:
        try:
            result = await db.execute(select(self.model).filter(filter_condition))
            return result.scalars().first()
        except SQLAlchemyError as e:
            logger.error(f"Database error in get: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error in get: {str(e)}")
            raise

    async def get_all(
        self, db: AsyncSession, page=None, page_size=None
    ) -> List[ModelType]:
        try:
            query = select(self.model)
            if page and page_size:
                query = query.offset((page - 1) * page_size).limit(page_size)
            result = await db.execute(query)
            return result.scalars().all()
        except SQLAlchemyError as e:
            logger.error(f"Database error in get_all: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error in get_all: {str(e)}")
            raise

    async def create(
        self, db: AsyncSession, obj_in: CreateSchemaType
    ) -> ModelType:
        try:
            obj_data = jsonable_encoder(obj_in)
            db_obj = self.model(**obj_data)
            db.add(db_obj)
            await db.commit()
            await db.refresh(db_obj)
            return db_obj
        except SQLAlchemyError as e:
            await db.rollback()
            logger.error(f"Database error in create: {str(e)}")
            raise
        except Exception as e:
            await db.rollback()
            logger.error(f"Unexpected error in create: {str(e)}")
            raise
    
    async def update_single(
        self, db: AsyncSession, *, db_obj: ModelType, obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        try:
            obj_data = jsonable_encoder(db_obj)
            
            if isinstance(obj_in, dict):
                update_data = obj_in
            else:
                update_data = obj_in.model_dump(exclude_unset=True) # 딕셔너리로 변환 True
            
            for field in obj_data:
                if field in update_data:
                    setattr(db_obj, field, update_data[field])
            
            db.add(db_obj)
            await db.commit()
            await db.refresh(db_obj)
            return db_obj
        
        except SQLAlchemyError as e:
            logger.error(f"Database error in update_single: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error in update_single: {str(e)}")
            raise

    async def update_many(
        self, db: AsyncSession, *, db_objs: List[ModelType], obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> List[ModelType]:
        try:
            if isinstance(obj_in, dict):
                update_data = obj_in
            else:
                update_data = obj_in.model_dump(exclude_unset=True) # 딕셔너리로 변환 True
            
            updated_objs = []
            for db_obj in db_objs:
                obj_data = jsonable_encoder(db_obj)
                for field in obj_data:
                    if field in update_data:
                        setattr(db_obj, field, update_data[field])
                
                db.add(db_obj)
                updated_objs.append(db_obj)
                
            await db.flush()  # 변경사항을 데이터베이스에 보냄
            await db.commit()   
            
            for obj in updated_objs:
                await db.refresh(obj)
        
            return updated_objs
        
        except SQLAlchemyError as e:
            logger.error(f"Database error in update_many: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error in update_many: {str(e)}")
            raise

    async def remove(
        self, db: AsyncSession, filter_condition: BinaryExpression
    ) -> ModelType:
        result = await db.execute(
            select(self.model).filter(filter_condition)
        )
        obj = result.scalars().first()
        if obj is None:
            return None
        await db.delete(obj)
        await db.commit()
        return obj