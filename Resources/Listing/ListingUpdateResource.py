from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from Resources.User import check_user_id
from Resources.Listing import check_listing_id, get_listingid_vehicleid, edit_listing_from_listing_id
from Resources.Vehicle import check_vehicle_id

class ListingUpdateResource(Resource):
    """
    ListingUpdateResource is used for updating an existing row in the Listing Table.
    Use HTTP PUT Method.
    Request must contain:
        access_token,
        vehicle_id,
        listing_id
    Request constrain:
        access_token must be linked to an existing user in the database,
        listing_id must be linked to an existing listing in the database,
        vehicle_id must be linked to an existing vehicle in the database.
    Responses:
        access_token is not linked to an existing user in the database:
            Response message: Your account can't be found.
            Response code: 404
        listing_id is not linked to an existing listing in the database:
            Response message: Listing does not exist.
            Response code: 404
        vehicle_id is not linked to an existing vehicle in the database:
            Response message: vehicle_is is not valid.
            Response code: 404
        listing updated:
            Response message: <listing_id>
            Response code: 200
    """
    @jwt_required()
    def post(self):
        listing_id, vehicle_id = get_listingid_vehicleid()

        current_user_id = get_jwt_identity()

        error = check_user_id(current_user_id)
        if error:
            return error
        error = check_listing_id(listing_id)
        if error:
            return error
        error = check_vehicle_id(vehicle_id)
        if error:
            return error
        listing_id  = edit_listing_from_listing_id(user_id=current_user_id, new_vehicle_id=vehicle_id)
        return {"listing_id", listing_id}, 200
    