from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity
from Resources.User import check_user_id

blacklist = set()

class UserLogoutResource(Resource):
    """
    UserLogoutResource is used to blacklist a jwt.
    Use HTTP POST method.
    Request must contain:
        access_token.
    Request constrain:
        access_token must be linked to an existing admin in the database.
    Responses:
        access_token is not linked to anyone:
            Response message: Your account can't be found.
            Response code: 404
        logged out:
            Respose message: You have logged out successfully.
            Response code: 200
    """
    @jwt_required()
    def post(self):
        current_user_id = get_jwt_identity()
        error = check_user_id(current_user_id)
        if error:
            return error

        jti = get_jwt()["jti"]
        blacklist.add(jti)
        return {"message": "You have logged out successfully."}, 200
