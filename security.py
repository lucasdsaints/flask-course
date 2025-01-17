from werkzeug.security import safe_str_cmp
from models.user import UserModel

# when access the /auth endpoint
def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user # the user is returned, the jwt is generated

# when access some endpoint that needs authentication 
def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)