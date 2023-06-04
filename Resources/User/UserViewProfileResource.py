from flask_restful import Resource
from Resources.User import get_user_name, check_user_name, view_user_from_user_name

class UserViewProfileResource(Resource):
    """
    UserViewProfileResource is used for accessing a user.
    Use HTTP GET.
    Request requirement:
        user_name.
    Request constrains:
        user_name must be linked to a user in the database.
    Responses:
        user_name is not linked to a user in the database:
            Response message: User not found.
            Response code: 404
        user:
            Response message: dict<user>
            Response code: 200
    """
    def get(self):
        user_name = get_user_name()
        in_use = check_user_name(user_name)
        if not in_use:
            return {"message": "User not found."}, 404
        return view_user_from_user_name(user_name), 200
        