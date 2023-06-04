from flask_restful import Resource
from Resources.User import get_user_name, check_user_name, view_user_from_user_name
from Resources.Comment import view_all_comments_from_user_id

class UserViewAllCommentsResource(Resource):
    """
    UserViewAllCommentsResource is used for accessing all comments a user has written.
    Use HTTP GET.
    Request requirement:
        user_name.
    Request constrains:
        user_name must be linked to a user in the database.
    Responses:
        user_name is not linked to a user in the database:
            Response message: User not found.
            Response code: 404
        comments:
            Response message: dict<comments>
            Response code: 200
    """
    def get(self):
        user_name = get_user_name()
        in_use = check_user_name(user_name)
        if not in_use:
            return {"message": "User not found."}, 404
        user = view_user_from_user_name(user_name)
        return view_all_comments_from_user_id(user["user_id"]), 200
