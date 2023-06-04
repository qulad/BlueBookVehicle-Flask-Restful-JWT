from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from Models.User.UserModel import User
from Models.Listing.ListingModel import Listing

class AdminViewPendingNewListingsResource(Resource):
    """
    AdminViewPendingNewListingsResource is used by admins to see which new listing are waiting for approval.
    Use HTTP GET method.
    Request must contain:
        access_token.
    Request constrains:
        access_token must be linked to an existing admin in the database.
    Responses:
        access_token is not linked to anyone:
            Response message: Your account can't be found.
            Response code: 404
        user does not have admin privilages:
            Response message: You don't have admin priviliges.
            Response code: 403
        no new listings found:
            Response message: There are no new listings waiting for approval.
            Response code: 204
        new listings found:
            Response message: list<new listings waiting for approval>
            Response code: 200
    """
    @jwt_required()
    def get(self):
        current_user_id = get_jwt_identity()
        current_user = User.query.filter_by(user_id=current_user_id).first()
        if not current_user:
            return {"message": "Your account can't be found."}, 404
        admin_privalige = current_user.is_admin
        if not admin_privalige:
            return {"message": "You don't have admin priviliges."}, 403
        listings = Listing.query.filter_by(new_waiting=True)
        if not listings.first():
            return {"message": "There are no new listings waiting for approval."}, 204
        return {"listings": [listing.to_dict() for listing in listings]}, 200
