from pydantic import BaseModel,Field,field_validator
from fastapi import Form,HTTPException

class UserValidator(BaseModel):
    full_name:str = Field(...,
                          min_length=3,
                          max_length=50,
                          description="نام باید بین 3 تا 50 کاراکتر باشد.")
    email:str = Field(...,
                      min_length=5,
                      max_length=100,
                      description="ایمیل باید بین 5 تا 100 کاراکتر باشد.")
    password:str = Field(...,
                         min_length=8,
                         max_length=50,
                         description="رمز عبور باید بین 8 تا 50 کاراکتر باشد.")
    @field_validator("email")
    def validate_email(cls, v):
        if "@" not in v:
            raise ValueError("ایمیل باید با @ شروع شود.")
        return v


def getUserDataFromForm(
    full_name:str = Form(...),
    email:str = Form(...),
    password:str = Form(...)
):
    try: 
        return UserValidator(full_name=full_name, email=email, password=password)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))