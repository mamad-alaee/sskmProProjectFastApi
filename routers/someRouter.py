from fastapi import APIRouter,HTTPException,Form,Depends
from pydantic import BaseModel,field_validator
from typing import Annotated

class SomeModel(BaseModel):
    name: str|None
    age: int|None

    @field_validator("age")
    def age_must_be_positive(cls, value):
        if type(value) is not int:
            raise ValueError("سن باید عددی باشد")
        if value is None:
            raise ValueError("سن نمیتواند خالی باشد")
        value = int(value)
        if not value > 0:
            raise ValueError("سن باید بزرگتر از 0 باشد")
        return value
    
    @field_validator("name")
    def name_must_not_be_empty(cls, value):
        if not value:
            raise ValueError("نام نمیتواند خالی باشد")
        if len(value) < 3:
            raise ValueError("نام باید دارای حداقل 3 کاراکتر باشد")
        return value
def get_some_model(
        name : Annotated[str|None,Form()]= None,
        age: Annotated[str|None,Form()]= None
        ):
    try:
        return SomeModel(name=name, age=age)
    except ValueError as e:
        errors = []
        for error in e.errors():
            errors.append(error['msg'].split(",")[1])
        raise HTTPException(status_code=400, detail=errors)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



some_router = APIRouter()

@some_router.post("/some_endpoint")
async def create_some_endpoint(some_model: SomeModel = Depends(get_some_model)):
    return {"status": "ok"}

@some_router.get("/some_endpoint")
async def some_endpoint():
    return "ok"

@some_router.delete("/some_endpoint/{age}")
async def delete_some_endpoint(age: int):

    if age < 18:
        raise HTTPException(status_code=403,
                             detail="You are not allowed to delete this resource")
    else:  
        return {"status": "ok"}