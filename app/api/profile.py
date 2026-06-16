from fastapi import APIRouter , Depends
from ..schema.profile import Profile ,Profile_response
from sqlalchemy.orm import session
from  ..db.database import get_db , Base , engine
from ..models.profile_db import profile


router = APIRouter()


Base.metadata.create_all(bind=engine)

@router.put("/login/profile" , response_model=Profile_response)
def profile_section(profiles : Profile , db : session=Depends(get_db)):
    profiles =  profile(
        reg_number= profiles.reg_number,
        name = profiles.name,
        age = profiles.age,
        email = profiles.email,
        course_enrolled= profiles.course_enrolled,
        department= profiles.department
    )

    db.add(profiles)
    db.commit()
    db.refresh(profiles)

    return profiles

