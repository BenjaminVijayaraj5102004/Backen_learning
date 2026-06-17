from pydantic import BaseModel , Field , EmailStr

class Profile(BaseModel):
    reg_number :int
    name : str
    age : int
    email : EmailStr
    course_enrolled : str 
    department : str 

class Profile_response(BaseModel):
    reg_number : int
    name : str
    age : int
    email : EmailStr
    course_enrolled : str 
    department : str 


class Profile_Update(BaseModel):
    name : str | None = None
    age : int | None = None
    email : EmailStr | None = None

