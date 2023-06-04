from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from Resources.User import check_user_id
from Resources.Listing import get_listingid, get_listing_details_from_listing_id, check_listing_id, delete_listing_from_listing_id
from Resources.Vehicle import check_vehicle_id, delete_vehicle_from_vehicle_id
from Resources.Comment import view_all_comments_from_listing_id, delete_comment_from_comment_id

class ListingDeleteResource(Resource):
    """
    ListingDeleteResource is used for deleting a row from Listing table.
    Use HTTP DELETE method.
    Request must contain:
        accesss_token,
        listing_id.
    Request constrain:
        access_token must be linked to a user in the database,
        listing_id must be linked to a listing in the database
        user_id must be the same as listing.user_id.
    Request Responses:
        access_token is not linked to a user in the database:
            Response Message: Your account can't be found.
            Response Code: 404
        listing_id is not linked to a user in the database:
            Response Message: Listing does not exist.
            Response Code: 404
        user_id is not same as listing.user_id:
            Response Message: This is not your listing.
            Response Code: 403
        listing deleted:
            Response Message: You have successfully deleted the listing.
            Response Code: 204
    """
    @jwt_required()
    def delete(self):
        listing_id = get_listingid()
        
        current_user_id = get_jwt_identity()
        error = check_user_id(current_user_id)
        if error:
            return error
        error = check_listing_id(listing_id)
        if error:
            return error
        listing = get_listing_details_from_listing_id(listing_id)
        same_user = (current_user_id == listing.listing_id)
        if not same_user:
            return {"message": "This is not your listing."}, 403
        error = check_vehicle_id(listing.vehicle_id)
        if not error:
            delete_vehicle_from_vehicle_id(error)
        comments = view_all_comments_from_listing_id(current_user_id)
        if type(comments) == dict:
            for comment in comments.values():
                delete_comment_from_comment_id(comment.comment_id)
        