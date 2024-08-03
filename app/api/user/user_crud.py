from database.models import User
from database.crud import CRUDBase
from api.user.user_schema import UserCreate, UserUpdate

class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    pass

user_crud = CRUDUser(User)