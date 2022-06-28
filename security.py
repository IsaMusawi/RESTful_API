from hmac import compare_digest
from models.user import UserModel


def authenticate(username, password):
    user = UserModel.findByUsername(username)
    if user and compare_digest(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.findById(user_id)