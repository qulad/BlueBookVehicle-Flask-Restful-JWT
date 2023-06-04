from flask_restful import Resource
from flask_jwt_extended import create_access_token
from Resources.User import get_username_password, check_user_name, check_userid_password, view_user_from_user_name

class UserLoginResource(Resource):
    """
    UserLoginResource is used for logging in an existing user.
    Use HTTP POST method.
    Request must contain:
        user_name,
        password.
    Request constrains:
        username must be in the database,
        password should be the same in the database.
    Responses:
        userame is not in the database:
            Response message: You don't have an account.
            Response code: 404
        password is not the same in the database:
            Response message: Wrong password.
            Response code: 401
        user logged in:
            Response message: access_token
            Response code 200
    """
    def post(self):
        user_name, password = get_username_password()
        
        user = check_user_name(user_name)
        if user:
            return {"message": "You don't have an acccount."}, 404
        user = view_user_from_user_name(user_name)
        same_password = check_userid_password(user_id=user.user_id, password1=password)
        if not same_password:
            return {"message": "Wrong password."}, 401
        access_token = create_access_token(identity=user.user_id)
        return {"access_token": access_token}, 200
