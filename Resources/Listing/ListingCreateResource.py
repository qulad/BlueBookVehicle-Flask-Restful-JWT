from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from Resources.User import check_user_id
from Resources.Listing import get_vehicle_id, add_listing
from Resources.Vehicle import check_vehicle_id

class ListingCreateResource(Resource):
    """
    ListingCreateResource is used for adding a new row to Listing Table.
    Use HTTP POST Method.
    Request must contain:
        access_token,
        vehicle_id.
    Request constrain:
        access_token must be linked to an existing user in the database,
        vehicle_id must be linked to an existing vehicle in the database.
    Responses:
        access_token is not linked to an existing user in the database:
            Response message: Your account can't be found.
            Response code: 404
        vehicle_id is not linked to an existing vehicle in the database:
            Response message: vehicle_is is not valid.
            Response code: 404
        listing created:
            Response message: <listing_id>
            Response code: 201 
    """
    @jwt_required()
    def post(self):
        vehicle_id = get_vehicle_id()

        current_user_id = get_jwt_identity()

        error = check_user_id(current_user_id)
        if error:
            return error
        error = check_vehicle_id(vehicle_id)
        if error:
            return error
        listing_id  = add_listing(user_id=current_user_id, vehicle_id=vehicle_id)
        return {"listing_id", listing_id}, 201
    