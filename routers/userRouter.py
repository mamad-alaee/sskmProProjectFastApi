from fastapi import APIRouter,Depends
from validators.userValidator import UserValidator,getUserDataFromForm
from controllers.userController import save_user
userRouter = APIRouter()


@userRouter.get("/users")
async def get_users():
    return {"job":"ok","message":"users"}

@userRouter.post("/users")
async def create_user(userData:UserValidator = Depends(getUserDataFromForm)):
    status , response = save_user(userData)
    if status:
        return {"job":"ok","message":f"user created successfully"}
    else:
        return {"job":"error","message":f"user creation failed {response}"}
    

@userRouter.put("/users/{id}")
async def update_user(id:int):
    return {"job":"ok","message":f"user with id {id} updated"}

@userRouter.delete("/users/{id}")
async def delete_user(id:int):
    return {"job":"ok","message":f"user with id {id} deleted"}