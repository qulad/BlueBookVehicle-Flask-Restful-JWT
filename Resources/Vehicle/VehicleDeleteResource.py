from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from Resources.User import check_user_id
from Resources.Vehicle import get_vehicleid, check_vehicle_id, check_user_owns_vehicle, delete_vehicle_from_vehicle_id
from Models import db
from Models.User.UserModel import User
from Models.Vehicle.VehicleModel import Vehicle

class VehicleDeleteResource(Resource):
    """
    VehicleViewDetailsResource is used for getting vehicle details from vehicle_id.
    Use HTTP DELETE method.
    Request must contain:
        access_token,
        vehicle_id.
    Request constrains:
        access_token must match the creator of vehicle,
        vehicle_id must be linked to an existing vehicle in the database.
    Responses:
        access_token is not linked to anyone:
            Response message: Your account can't be found.
            Response code: 404
        vehicle_id is not linked to an existing vehicle in the database:
            Response message: Vehicle can't be found.
            Response code: 404
        user did not create vehicle:
            Response message: This is not your vehicle.
            Response code: 403
        vehicle is deleted:
            Response message: You have successfully deleted a vehicle.
            Response code: 204
    """
    @jwt_required()
    def delete(self):
        vehicle_id = get_vehicleid()

        current_user_id = get_jwt_identity()
        check_user_id(current_user_id)
        vehicle = check_vehicle_id(vehicle_id)
        if vehicle:
            return {"message": "Vehicle can't be found."}, 404
        different_user = check_user_owns_vehicle(user_id=current_user_id, vehicle_id=vehicle_id)
        if not different_user:
            return {"message": "This is not your vehicle."}, 403
        delete_vehicle_from_vehicle_id(vehicle_id)
        return {"message": "You have successfully deleted a vehicle."}, 204
