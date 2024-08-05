from database.models import User
from database.crud import CRUDBase
from api.user.user_schema import UserCreate, UserUpdate

class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    pass

learning_crud = CRUDUser(User) #Learning 모델로 변경