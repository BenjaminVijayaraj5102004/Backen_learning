from fastapi import APIRouter ,Depends
from sqlalchemy.orm import session 
from ..schema.loggin import Loggin , Loggin_response
from ..db.database import get_db , Base , engine
from ..models.login_db import Login 

from ..core.config import settings 
from ..core.security import hash_password , verfiy_password



router = APIRouter()

Base.metadata.create_all(bind=engine)

@router.put("/login" , response_model=Loggin_response )
def login_section (loggin : Loggin , db : session=Depends(get_db)):
    login = Login(
        email = loggin.email,
        password = hash_password(loggin.password)
    )
    db.add(login)
    db.commit()
    db.refresh(login)
    
    
    return login
