from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from configparser import ConfigParser
from Models import db
from __init__ import load_api_endpoints
import datetime

app = Flask(__name__)
config = ConfigParser()
config.read("config.ini")

app.config["SQLALCHEMY_DATABASE_URI"] = config.get("DEFAULT", "SQLALCHEMY_DATABASE_URI")
app.config["JWT_SECRET_KEY"] = config.get("DEFAULT", "JWT_SECRET_KEY")
app.config["JWT_TOKEN_LOCATION"] = config.get("DEFAULT", "JWT_TOKEN_LOCATION").split(",")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = config.get("DEFAULT", "JWT_ACCESS_TOKEN_EXPIRES")
app.config["JWT_EXPIRATION_DELTA"] = datetime.timedelta(days=10)

api = Api(app, prefix="/api/v1/")
jwt = JWTManager(app)
db.init_app(app)

load_api_endpoints(api)

if (__name__ == "__main__"):
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)
