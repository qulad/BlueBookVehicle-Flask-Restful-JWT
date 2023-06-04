from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from Resources.Admin import get_listingid
from Models.User.UserModel import User
from Models.Listing.ListingModel import Listing
from Models import db

class AdminAcceptPendingNewListingResource(Resource):
    """
    AdminAcceptPendingNewListingsResource is used by admins to approve new listing are waiting for approval.
    Use HTTP POST method.
    Request must contain:
        access_token,
        listing_id.
    Request constrains:
        access_token must be linked to an existing admin in the database,
        listing_id must be linked to an existing listing that is waiting for new approval in the database.
    Responses:
        access_token is not linked to anyone:
            Response message: Your account can't be found.
            Response code: 404
        user does not have admin privilages:
            Response message: You don't have admin priviliges.
            Response code: 403
        listing_id is not linked to any listing:
            Response message: Listing can't be found.
            Response code: 404
        listing is not waiting for new approval:
            Response message: Listing is already approved.
            Response code: 403
        listing is approved:
            Response message: Listing is approved.
            Response code: 200
    """
    @jwt_required()
    def post(self):
        listing_id = get_listingid()

        current_user_id = get_jwt_identity()
        current_user = User.query.filter_by(user_id=current_user_id).first()
        if not current_user:
            return {"message": "Your account can't be found."}, 404
        admin_privalige = current_user.is_admin
        if not admin_privalige:
            return {"message": "You don't have admin priviliges."}, 403
        listing = Listing.query.filter_by(listing_id=listing_id)
        if not listing.first():
            return {"message": "Listing can't be found."}, 404
        waiting_for_approval = listing.new_waiting
        if not waiting_for_approval:
            return {"message": "Listing is already approved."}, 403
        
        listing.new_waiting = False
        db.session.commit()
        return {"message", "Listing is approved."}, 200
    