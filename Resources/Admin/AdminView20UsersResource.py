from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from Models import db
from Models.User.UserModel import User
from Resources.Admin import get_upperrange

class AdminView20UsersResource(Resource):
    """
    AdminView20UsersResource is used by admins to see everything about the users.
    Use HTTP GET method.
    Request must contain:
        access_token,
        upper_range 20.
    Request constrains:
        access_token must be linked to an existing admin in the database,
        upper_range must be lower than user count in the database,
        lower_range must be lower or equal to one.
    Responses:
        access_token is not linked to anyone:
            Response message: Your account can't be found.
            Response code: 404
        user does not have admin privilages:
            Response message: You don't have admin priviliges.
            Response code: 403
        upper_range is bigger than user count:
            Response message: upper_range is out of range.
            Response code: 417
        lower_range is equal or lower than zero:
            Response message: lower range is out of range.
            Response code: 417
        users are not found:
            Response message: Users are not found.
            Response code: 404
        users are found:
            Response message: list<users>
            Response code: 200
    """
    @jwt_required
    def get(self):
        upper_range = get_upperrange()
        lower_range = upper_range - 20

        current_user_id = get_jwt_identity()
        current_user = User.query.filter_by(user_id=current_user_id).first()
        if not current_user:
            return {"message": "Your account can't be found."}, 404
        admin_privalige = current_user.is_admin
        if not admin_privalige:
            return {"message": "You don't have admin priviliges."}, 403
        row_count = User.query.count()
        if upper_range > row_count:
            return {"message": "upper_range is out of range."}, 417
        if lower_range <= 0:
            return {"message": "lower range is out of range."}, 417
        users = User.query.filter(User.user_id.in_([lower_range, upper_range]))
        if not users.first():
            return {"message": "Users are not found."}, 404
        return {"Users": [user.to_dict() for user in users]}, 200
