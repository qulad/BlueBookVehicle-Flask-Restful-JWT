from flask_restful import Resource
from Resources.Comment import get_commentid, check_comment_id, view_comment_from_comment_id

class CommentViewSingleResource(Resource):
    """
    CommentViewSingleResource is used for viewing a single comment.
    Use HTTP GET method.
    Request must contain:
        comment_id,
    Request constrains:
        comment_id must be linked to an existing comment in the database.
    Responses:
        comment_id is not linked to any comment:
            Response message: Comment can't be found.
            Response code: 404
        comment is found:
            Response message: dict<comment>.
            Response code: 200
    """
    def get(self):
        comment_id = get_commentid()

        check_comment_id(comment_id)
        comment_data = view_comment_from_comment_id(comment_id)
        return comment_data, 200
    