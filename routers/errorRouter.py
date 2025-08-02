from fastapi import APIRouter,Form,Header
from controllers.authController import decode_access_token

error_router = APIRouter()

@error_router.get("/error")
async def error(name: str=Form(...),jwt_token: str=Header(...)):
    userData = decode_access_token(jwt_token)
    raise Exception(f"user with this id => {userData["_id"]} send get request to this path /error and the name is {name} ")