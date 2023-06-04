from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from Resources.Comment import get_commentid_comment, check_comment_id, check_user_id_owns_comment_id, edit_comment_from_comment_id
from Resources.User import check_user_id

class CommentEditResource(Resource):
    """
    CommentEditResource is used to edit a row to Comment table.
    Use HTTP PUT method.
    Request must contain:
        access_token,
        comment_id,
        comment.
    Request constrains:
        access_token must be linked to an existing admin in the database,
        listing_id must be linked to an existing listing in the database,
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
        comment added:
            Response message: <comment_id>
            Response code: 200
    """
    @jwt_required()
    def put(self):
        comment_id, comment_text = get_commentid_comment()

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
        edit_comment_from_comment_id(comment_id=comment_id, comment_text=comment_text)
        return {"comment_id": comment_id}, 200
    