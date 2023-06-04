from flask_restful import Resource
from flask_jwt_extended import create_access_token
from Resources.User import get_email_password1_password2, get_non_credentials, check_email, check_user_name, add_user

class UserRegisterResource(Resource):
    """
    UserRegisterResource is used for creating a new user.
    Use HTTP POST method.
    Request must contain: 
        email,
        password1,
        password2,
        first_name,
        last_name,
        user_name,
        phone_number,
        profile_image_url,
        birth_date.
    Request constrains:
        email must be unique,
        password1 and password2 must be same,
        user_name must be unique.
    Responses:
        email not unique:
            Response message: You already have an account.
            Response code: 409
        password1 and password2 are not same:
            Response message: Passwords must be the same.
            Response code: 400
        user_name not unique:
            Response message: This user_name is taken.
            Response code: 409
        user created:
            Response message: access_token
            Response code: 201
    """
    def post(self):
        email, password1, password2 = get_email_password1_password2()
        print(password1, password2)
        args = get_non_credentials()

        existing_email = check_email(email)
        if existing_email:
            return existing_email
        existing_username = check_user_name(args["user_name"])
        if existing_username:
            return existing_username
        different_passwords = (password1 != password2)
        if different_passwords:
            return {"message": "Passwords must be the same."}, 400
        new_user_id = add_user(first_name=args["first_name"], last_name=args["last_name"], user_name=args["user_name"], phone_number=args["phone_number"], profile_image_url=args["profile_image_url"], email=email, password=password1, birth_date=args["birth_date"])
        access_token = create_access_token(identity=new_user_id)
        return {"access_token": access_token}, 201
