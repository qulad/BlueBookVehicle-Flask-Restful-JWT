from flask import request
from flask_restful import reqparse
from Models import db
from Models.User.UserModel import User

def get_email_password():
    email = request.json.get("email")
    password = request.json.get("password")
    return email, password

def get_username_password():
    user_name = request.json.get("user_name")
    password = request.json.get("password")
    return user_name, password

def get_email_password1_password2():
    email = request.json.get("email")
    password1 = request.json.get("password1")
    password2 = request.json.get("password2")
    return email, password1, password2

def get_non_credentials():
    parser = reqparse.RequestParser()
    parser.add_argument("first_name", type=str, required=True)
    parser.add_argument("last_name", type=str, required=True)
    parser.add_argument("user_name", type=str, required=True)
    parser.add_argument("phone_number", type=str, required=True)
    parser.add_argument("profile_image_url", type=str, required=True)
    parser.add_argument("birth_date", type=str, required=True)
    arg = parser.parse_args()
    return arg

def get_user_name():
    parser = reqparse.RequestParser()
    parser.add_argument("user_name", type=str, required=True)
    arg = parser.parse_args()
    return arg ["user_name"]

def get_password1_password2():
    password1 = request.json.get("password1")
    password2 = request.json.get("password2")
    return password1, password2

def check_user_id(user_id):
    user_id_valid = User.query.filter_by(user_id=user_id).first()
    if not user_id_valid:
        return {"message": "User can't be found."}, 404

def check_user_name(user_name):
    user_name_taken = User.query.filter_by(user_name=user_name).first()
    if user_name_taken:
        return {"message": "User name is taken."}, 409

def check_email(email):
    email_taken = User.query.filter_by(email=email).first()
    if email_taken:
        return {"message": "You have an account."}, 409

def check_userid_password(user_id, password1):
    user = User.query.filter_by(user_id=user_id)
    return user.check_password(password1)

def view_user_from_user_id(user_id):
    user = User.query.filter_by(user_id=user_id).first()
    data = {
        "user_id": user.user_id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "user_name": user.name,
        "phone_number": user.phone_number,
        "profile_image_url": user.get_profile_image_url(),
        "email": user.email,
        "birth_date": user.birth_date
    }
    return data

def view_user_from_user_name(user_name):
    user = User.query.filter_by(user_name=user_name).first()
    data = {
        "user_id": user.user_id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "user_name": user.user_name,
        "phone_number": user.phone_number,
        "profile_image_url": user.get_profile_image_url(),
        "email": user.email,
        "birth_date": user.birth_date
    }
    return data

def add_user(first_name, last_name, user_name, phone_number, profile_image_url, email, password, birth_date):
    new_user = User()
    new_user.set_first_name(first_name)
    new_user.set_last_name(last_name)
    new_user.set_user_name(user_name)
    new_user.set_phone_number(phone_number)
    new_user.set_profile_image_url(profile_image_url)
    new_user.set_birth_date(birth_date)
    new_user.set_email(email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return new_user.user_id

def edit_user_table_from_user_id(user_id, first_name, last_name, user_name, phone_number, profile_image_url, email, password, birth_date):
    user = User.query.filter_by(user_id=user_id)
    user.set_first_name(first_name)
    user.set_last_name(last_name)
    user.set_user_name(user_name)
    user.set_phone_number(phone_number)
    user.set_profile_image_url(profile_image_url)
    user.set_birth_date(birth_date)
    user.set_email(email)
    user.set_password(password)
    db.session.commit()
    return user.user_id

def edit_user_password_from_user_id(user_id, password):
    user = User.query.filter_by(user_id=user_id)
    user.set(password)
    db.session.commit()

def delete_user_from_user_id(user_id):
    user = User.query.filter_by(user_id=user_id)
    db.session.delete(user)
    db.session.commit()
