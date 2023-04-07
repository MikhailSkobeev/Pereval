from fastapi import APIRouter, Depends
from schem import UserBase, UserDisplay
from sqlalchemy.orm.session import Session
from DateBase.dateb import get_db
from DateBase import DB_user


router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.post('', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return DB_user.create_user(db, request)