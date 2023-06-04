from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from Resources.Admin import get_commentid
from Models.User.UserModel import User
from Models.Comment.CommentModel import Comment
from Models import db

class AdminDeleteCommentResource(Resource):
    """
    AdminDeleteCommenttResource is used by admins to delete comments on a post.
    Use HTTP DELETE method.
    Request must contain:
        access_token,
        comment_id.
    Request constrains:
        access_token must be linked to an existing admin in the database,
        comment_id must be linked to an existing comment in the database.
    Responses:
        access_token is not linked to anyone:
            Response message: Your account can't be found.
            Response code: 404
        user does not have admin privilages:
            Response message: You don't have admin priviliges.
            Response code: 403
        comment_id is not linked to any comment:
            Response message: Comment can't be found.
            Response code: 404
        comment deleted:
            Response message: You have successfully deleted the comment.
            Response code: 204
    """
    @jwt_required()
    def delete(self):
        comment_id = get_commentid()

        current_user_id = get_jwt_identity()
        current_user = User.query.filter_by(user_id=current_user_id).first()
        if not current_user:
            return {"message": "Your account can't be found."}, 404
        admin_privalige = current_user.is_admin
        if not admin_privalige:
            return {"message": "You don't have admin priviliges."}, 403
        comment = Comment.query.filter_by(comment_id=comment_id)
        if not comment.first():
            return {"message": "Comment can't be found."}, 404

        db.session.delete(comment)
        db.session.commit()
        
        return {"message": "You have successfully deleted the comment."}, 204
