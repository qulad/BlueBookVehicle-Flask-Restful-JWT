from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from Resources.Comment import get_listingid_comment, add_comment
from Resources.User import check_user_id
from Resources.Listing import check_listing_id

class CommentAddResource(Resource):
    """
    CommentAddResource is used to add a row to Comment table.
    Use HTTP POST method.
    Request must contain:
        access_token,
        listing_id,
        comment.
    Request constrains:
        access_token must be linked to an existing admin in the database,
        listing_id must be linked to an existing listing in the database,
    Responses:
        access_token is not linked to anyone:
            Response message: User can't be found.
            Response code: 404
        listing_id is not linked to any listing:
            Response message: Listing can't be found.
            Response code: 404
        comment added:
            Response message: <comment_id>
            Response code: 201
    """
    @jwt_required()
    def post(self):
        listing_id, comment_text = get_listingid_comment()

        current_user_id = get_jwt_identity()
        error = check_user_id(current_user_id)
        if error:
            return error
        error = check_listing_id(listing_id)
        if error:
            return error
        comment_id = add_comment(user_id=current_user_id, listing_id=listing_id, comment=comment_text)
        return {"comment_id": comment_id}, 201
    