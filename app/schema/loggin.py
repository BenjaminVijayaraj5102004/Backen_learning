from pydantic import BaseModel , Field ,EmailStr


class Loggin(BaseModel):
    email : EmailStr
    password : str = Field(max_length=8)


class Loggin_response(BaseModel):
    id: int
    email : EmailStr


