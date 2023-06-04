from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from Resources.User import get_password1_password2, check_user_id, edit_user_password_from_user_id

class UserResetPasswordResource(Resource):
    """
    UserResetPasswordResource is used for changing a users password.
    Use HTTP PUT method.
    Request must contain:
        access_token,
        password1,
        password2,
    Request constrains:
        access_token must be linked to an existing user in the database,
        password1 and password2 must be same.
    Responses:
        access_token is not linked to an existing user in the database:
            Response message: Your account can't be found.
            Response code: 404
        password1 and password2 are not same:
            Response message: Passwords must be the same.
            Response code: 400
        user updated:
            Response message: You have successfully changed your password.
            Response code: 200
    """
    @jwt_required()
    def put(self):
        password1, password2 = get_password1_password2()

        current_user_id = get_jwt_identity()
        error = check_user_id(current_user_id)
        if error:
            return error
        different_passwords = (password1 != password2)
        if different_passwords:
            return {"message": "Passwords must be the same."}, 400
        edit_user_password_from_user_id(user_id=current_user_id, password=password1)
        return {"message": "You have succesfully changed your password."}, 200
