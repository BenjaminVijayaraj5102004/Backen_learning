from fastapi import FastAPI
from app.api.loggin_route import router as login_route
from app.api.profile import router as profile_route
from app.api.token_route import router as token_route

app = FastAPI()
app.include_router(login_route)
app.include_router(profile_route)
app.include_router(token_route)