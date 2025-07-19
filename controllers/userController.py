from models.userModel import User
from fastapi import HTTPException
from bson.objectid import ObjectId
from datetime import datetime, timedelta
from jose import jwt

def save_user(userData):
    try:
        userData = dict(userData)
        if not check_user_exists(userData['email']):
            created_user = User(**userData).save()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"job":"ok","data":str(created_user)}
    

def get_all_users(page,limit):
    try:
        skip = (page-1)*limit
        userList = list(User.objects().skip(skip).limit(limit).as_pymongo())
        for user in userList:
            user['_id'] = str(user['_id'])
        return {"job":"ok","data":userList}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def edit_user(user_id,userData):
    try:
        user = User.objects(id=ObjectId(user_id))
        user.update(**dict(userData))
        return {"job":"ok","data":str(user)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def delete_user_with_id(user_id):
    try:
        user = User.objects(id=ObjectId(user_id))
        user.delete()
        return {"job":"ok","data":"user deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def check_user_exists(email):
    try:
        user = list(User.objects(email=email).as_pymongo())
        if len(user) > 0:
            raise HTTPException(status_code=400, detail="User already exists")
        else:
            return False
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def login_user(loginData):
    try:
        founded_user = list(User.objects(email=loginData['email']).as_pymongo())
        if len(founded_user) > 0 :
            founded_user = founded_user[0]
            if founded_user['password'] == loginData['password']:
                return create_access_token(founded_user)
            else:
                raise HTTPException(status_code=401, detail="رمز عبور اشتباه است")
        else:
            raise HTTPException(status_code=404, detail="کاربری با این ایمیل یافت نشد")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def create_access_token(founded_user):
    try:
        # expire_time = timedelta(days=2)
        userData = {
            "_id": str(founded_user['_id']),
            "full_name" : founded_user['full_name'],
            "email" : founded_user['email'],
        }
        access_token = jwt.encode(userData,key="mamadHasanQoli@9994444",algorithm="HS256")
        return {"job":"ok","access_token":access_token}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def decode_access_token(access_token):
    try:
        decoded_token = jwt.decode(access_token,key="mamadHasanQoli@9994444",algorithms=["HS256"])
        return decoded_token
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))