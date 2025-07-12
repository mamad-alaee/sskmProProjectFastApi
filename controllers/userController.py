from models.userModel import User


def save_user(userData):
    try:   
        created_user = User(**dict(userData)).save()
    except Exception as e:
        return False, str(e)
    return True, created_user.to_mongo()
    