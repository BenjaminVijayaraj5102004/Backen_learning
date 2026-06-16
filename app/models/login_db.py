from sqlalchemy import Column, Integer, String
from ..db.database import Base

class Login(Base):
    __tablename__ = "login"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

