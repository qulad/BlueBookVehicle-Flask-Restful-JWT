from flask import url_for
from datetime import datetime
from Models import db, bcrypt, default_image_url

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    user_name = db.Column(db.String(60), nullable=False, unique=True)
    phone_number = db.Column(db.String(16), nullable=False)
    profile_image_url = db.Column(db.String(200), nullable=False, default=default_image_url)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    birth_date = db.Column(db.String(100), nullable=False)
    joined_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    is_admin = db.Column(db.Boolean, nullable=False, default=0)

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_user_name(self, user_name):
        self.user_name = user_name

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number
    
    def set_profile_image_url(self, profile_image_url):
        self.profile_image_url = profile_image_url

    def set_birth_date(self, birth_date):
        self.birth_date = birth_date

    def set_email(self, email):
        self.email = email

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, pass_):
        return bcrypt.check_password_hash(self.password, pass_)
    
    def get_profile_image_url(self):
        profile_image_url = self.profile_image_url
        return profile_image_url

    def to_dict(self):
        return {
            c.name: getattr(self, c.name) for c in self.__table__.columns
            if c.name not in ["created_at", "edited_at"]
        }
    