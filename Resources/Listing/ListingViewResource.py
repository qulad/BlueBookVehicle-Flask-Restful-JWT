from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity
from Resources.User import check_user_id
from Resources.Listing import get_listingid, get_listing_details_from_listing_id, check_listing_id, view_listing_detail_from_listing_id
from Resources.Vehicle import check_vehicle_id

class ListingViewResource(Resource):
    """
    ListingViewResource is used for viewing a row from Listing Table.
    Use HTTP Get Method.
    Request must contain:
        listing_id.
    Request constrains:
        listing_id must be linked to a listing in the database,
    Responses:
        listing_id is not linked to a listing in the database:
            Response message: Listing does not exist.
            Response code: 404
        vehicle_id is not linked to a vehicle in the database:
            Response message: Vehicle does not exist.
            Response code: 404
        user_id is not linked to a user in the database:
            Response message: User does not exist.
            Response code: 404
        listing is active:
            Response message: dict<listing>
            Response code: 200
        listing is not active:
            access_token is absent:
                Response message: Forbidden
                Response code: 403
            access_token does not match user_id:
                Response message: Forbidden
                Response code: 403
            access_token does match user_id:
                Response message: dict<listing>
                Response code: 200
    """
    def get(self):
        listing_id = get_listingid()

        error = check_listing_id(listing_id)
        if error:
            return error
        listing = get_listing_details_from_listing_id(listing_id)
        error = check_vehicle_id(listing.vehicle_id)
        if error:
            return error
        error = check_user_id(listing.user_id)
        if error:
            return error
        if listing.listing_active:
            data = view_listing_detail_from_listing_id(listing_id)
            return data, 200
        else:
            current_user = get_jwt_identity()
            if not current_user:
                return {"message": "Forbidden"}, 403
            else:
                same_user = (current_user == listing)
                if not same_user:
                    return {"message": "Forbidden"}, 403
                else:
                    data = view_listing_detail_from_listing_id(listing_id)
                    return data, 200
