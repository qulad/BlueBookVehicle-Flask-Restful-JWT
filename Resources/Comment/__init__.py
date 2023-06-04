from datetime import datetime
from flask_restful import reqparse
from Models import db
from Models.Comment.CommentModel import Comment
from Resources.User import check_user_id, view_user_from_user_id

def get_listingid_comment():
    parser = reqparse.RequestParser()
    parser.add_argument("listing_id", type=int, required=True)
    parser.add_argument("comment", type=str, required=True)
    args = parser.parse_args()
    return args["listing_id"], args["comment"]

def get_commentid():
    parser = reqparse.RequestParser()
    parser.add_argument("comment_id", type=int, required=True)
    args = parser.parse_args()
    return args["comment_id"]

def get_commentid_comment():
    parser = reqparse.RequestParser()
    parser.add_argument("comment_id", type=int, required=True)
    parser.add_argument("comment", type=str, required=True)
    args = parser.parse_args()
    return args["comment_id"], args["comment"]

def check_comment_id(comment_id):
    comment_id_valid = Comment.query.filter_by(comment_id=comment_id).first()
    if not comment_id_valid:
        return {"message": "Comment can't be found."}, 404

def check_comment_upper_range(upper_range):
    row_count = Comment.query.count()
    if upper_range > row_count:
        return {"message": "upper_range is out of range."}, 417

def check_user_id_owns_comment_id(user_id, comment_id):
    comment = Comment.query.filter_by(comment_id=comment_id)
    same_user = (comment.user_id == user_id)
    if not same_user:
        return {"message": "This comment doesn't belong to you."}, 403

def view_comment_from_comment_id(comment_id):
    comment = Comment.query.filter_by(comment_id=comment_id)
    user_validation = check_user_id(comment.user_id)
    if type(user_validation) == tuple:
        delete_comment_from_comment_id
        return {"message": "Can't find commenter."}, 424
    user = view_user_from_user_id(comment.user_id)
    data = {
        "comment_id": comment.comment_id,
        "user": user,
        "listing_id": comment.listing_id,
        "comment": comment.comment,
        "comment_edited": comment.edited
    }
    return data

def view_all_comments_from_user_id(user_id):
    comments = Comment.query.filter_by(user_id=user_id)
    if not comments.first():
        return {"message": "There are no comments."}, 404
    comments = list(comments.all())
    output = {}
    for i in range(len(comments)):
        comment = comments[i]
        if not comment:
            break
        user_validation = check_user_id(comment.user_id)
        if type(user_validation) == tuple:
            delete_comment_from_comment_id
            return {"message": "Can't find commenter."}, 424
        user = view_user_from_user_id(comment.user_id)
        data = {
            "comment_id": comment.comment_id,
            "user": user,
            "listing_id": comment.listing_id,
            "comment": comment.comment,
            "comment_edited": comment.edited
        }
        output[f"comment {i}"] = data
    return output

def view_all_comments_from_user_id_within_range(user_id, lower_range, upper_range):
    comments = Comment.query.filter_by(user_id=user_id)
    if not comments.first():
        return {"message": "There are no comments."}, 404
    comments = list(comments.all())[(lower_range-1):upper_range]
    output = {}
    for i in range(len(comments)):
        comment = comments[i]
        if not comment:
            break
        user_validation = check_user_id(comment.user_id)
        if type(user_validation) == tuple:
            delete_comment_from_comment_id
            return {"message": "Can't find commenter."}, 424
        user = view_user_from_user_id(comment.user_id)
        data = {
            "comment_id": comment.comment_id,
            "user": user,
            "listing_id": comment.listing_id,
            "comment": comment.comment,
            "comment_edited": comment.edited
        }
        output[f"comment {i}"] = data
    return output, 200

def view_all_comments_from_listing_id(listing_id):
    comments = Comment.query.filter_by(listing_id=listing_id)
    if not comments.first():
        return {"message": "There are no comments."}, 404
    comments = list(comments.all())
    output = {}
    for i in range(len(comments)):
        comment = comments[i]
        if not comment:
            break
        user_validation = check_user_id(comment.user_id)
        if type(user_validation) == tuple:
            delete_comment_from_comment_id
            return {"message": "Can't find commenter."}, 424
        user = view_user_from_user_id(comment.user_id)
        data = {
            "comment_id": comment.comment_id,
            "user": user,
            "listing_id": comment.listing_id,
            "comment": comment.comment,
            "comment_edited": comment.edited
        }
        output[f"comment {i}"] = data
    return output

def view_comment_from_listing_id_within_range(listing_id, lower_range, upper_range):
    comments = Comment.query.filter_by(listing_id=listing_id)
    if not comments.first():
        return {"message": "There are no comments."}, 404
    comments = list(comments.all())[(lower_range-1):upper_range]
    output = {}
    for i in range(len(comments)):
        comment = comments[i]
        user_validation = check_user_id(comment.user_id)
        if type(user_validation) == tuple:
            delete_comment_from_comment_id
            return {"message": "Can't find commenter."}, 424
        user = view_user_from_user_id(comment.user_id)
        data = {
            "comment_id": comment.comment_id,
            "user": user,
            "listing_id": comment.listing_id,
            "comment": comment.comment,
            "comment_edited": comment.edited
        }
        output[f"comment {i}"] = data
    return output

def add_comment(user_id, listing_id, comment):
    new_comment = Comment(user_id, listing_id, comment)
    db.session.add(new_comment)
    db.session.commit()
    return new_comment.comment_id

def edit_comment_from_comment_id(comment_id, comment_text):
    comment = Comment.query.filter_by(comment_id=comment_id)
    comment.comment = comment_text
    comment.edited = True
    comment.edited_at = datetime.now()
    db.session.commit()
    return comment.comment_id

def delete_comment_from_comment_id(comment_id):
    comment = Comment.query.filter_by(comment_id=comment_id).first()
    db.session.delete(comment)
    db.session.commit()

