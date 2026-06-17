from fastapi import APIRouter , Depends
from ..schema.profile import Profile_Update , Profile_response
from sqlalchemy.orm import Session
from  ..db.database import get_db , Base , engine
from ..models.profile_db import profile
from ..core.security import Current_user

router = APIRouter()


Base.metadata.create_all(bind=engine)


@router.patch("/login/profile/update/{id}", response_model=Profile_response)
def update_profile(
    id: int,
    profile_update: Profile_Update,
    db: Session = Depends(get_db)
):
    db_profile = db.query(profile).filter(profile.reg_number == id).first()

    if not db_profile:
        return {"error": "Profile not found"}

    update_data = profile_update.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_profile, key, value)

    db.commit()
    db.refresh(db_profile)

    return db_profile