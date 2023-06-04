from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from Resources.User import get_non_credentials, get_email_password1_password2, check_user_id, check_userid_password, edit_user_table_from_user_id

class UserEditResource(Resource):
    """
    UserEditResource is used for updating a existing user.
    Use HTTP PUT method.
    Request must contain:
        access_token,
        email,
        password1,
        password2,
        first_name,
        last_name,
        phone_number,
        birth_date.
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
            Response message: You have successfully updated your profile.
            Response code: 200
    """
    @jwt_required()
    def put(self):
        email, password1, password2 = get_email_password1_password2()
        args = get_non_credentials()

        current_user_id = get_jwt_identity()
        error = check_user_id(current_user_id)
        if error:
            return error
        different_passwords = (password1 != password2)
        if different_passwords:
            return {"message": "Passwords must be the same."}, 400
        same_password = check_userid_password(user_id=current_user_id, password1=password1)
        if not same_password:
            return {"message": "Wrong password."}, 401
        edit_user_table_from_user_id(user_id=current_user_id, first_name=args["first_name"], last_name=args["last_name"], user_name=args["user_name"], phone_number=args["phone_number"], profile_image_url=args["profile_image_url"], email=email, password=password1, birth_date=args["birth_date"])
        return {"message": "You have succesfully updated your profile."}, 200
