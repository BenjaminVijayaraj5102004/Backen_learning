from fastapi import APIRouter ,Depends ,HTTPException
from ..schema.token import Token
from ..schema.loggin import Loggin
from ..core.security import create_access_token,verify_access_token,verfiy_password
from ..models.login_db import Login 
from ..db.database import get_db , Base , engine
from sqlalchemy.orm import Session
from ..core.security import oauth2_scheme

router = APIRouter()

@router.post("/login/Token" , response_model=Token )

def check_authention(
    loggin: Loggin,
    db: Session = Depends(get_db)
):
    db_user = (
        db.query(Login)
        .filter(Login.email == loggin.email)
        .first()
    )

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email"
        )

    if not verfiy_password(
        loggin.password,
        db_user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    access_token = create_access_token(
        data={"sub": db_user.email}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }




@router.get("/me")
def me(token: str = Depends(oauth2_scheme)):
    return {"token": token}