from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from Resources.Comment import get_commentid, check_comment_id, delete_comment_from_comment_id, check_user_id_owns_comment_id
from Resources.User import check_user_id

class CemmentDeleteResource(Resource):
    """
    CommentDeleteResource is used for deleting row from Comment table.
    Use HTTP DELETE method.
    Request must contain:
        access_token,
        comment_id.
    Request constrains:
        access_token must be linked to an existing user in the database,
        comment_id must be linked to an existing comment in the database.
    Responses:
        access_token is not linked to anyone:
            Response message: User can't be found.
            Response code: 404
        comment_id is not linked to any comment:
            Response message: Comment can't be found.
            Response code: 404
        comment doesn't belong to do user:
            Response message: This comment doesn't belong to you.
            Response code: 403
        comment deleted:
            Response message: You have successfully deleted your comment.
            Response code: 204
    """
    @jwt_required()
    def delete(self):
        comment_id = get_commentid()

        current_user_id = get_jwt_identity()
        error = check_user_id(current_user_id)
        if error:
            return error
        error = check_comment_id(comment_id)
        if error:
            return error
        error = check_user_id_owns_comment_id(user_id=current_user_id, comment_id=comment_id)
        if error:
            return error
        delete_comment_from_comment_id(comment_id)
        return {"message": "You have successfully deleted your comment."}, 204
    