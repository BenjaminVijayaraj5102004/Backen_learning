from sqlalchemy import String , Integer , ForeignKey ,Column
from ..db.database import Base
from ..models.login_db import Login

class profile(Base):
    __tablename__ = "profile"
    reg_number = Column(Integer , ForeignKey(Login.id),primary_key=True)
    name = Column(String , nullable=False)
    age = Column(Integer , nullable=False)
    course_enrolled = Column(String)
    email = Column(String , nullable=False)
    department = Column(String)