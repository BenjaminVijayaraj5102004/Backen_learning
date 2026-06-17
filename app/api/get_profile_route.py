from fastapi import APIRouter , Depends ,Query
from ..schema.profile import Profile ,Profile_response
from sqlalchemy.orm import Session
from  ..db.database import get_db , Base , engine
from ..models.profile_db import profile
from ..core.security import Current_user


router = APIRouter()


Base.metadata.create_all(bind=engine)

@router.get("/login/profile/" , response_model=Profile_response)
def get_profile_id (id : int =Query(), db : Session = Depends(get_db) ):
    
    user_profile = db.query(profile).filter(profile.reg_number == id).first()


    return user_profile