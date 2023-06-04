from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from Resources.Admin import get_upperrange
from Models import db
from Models.User.UserModel import User
from Models.Vehicle.VehicleModel import Vehicle
from Models.Vehicle.VehicleBodyModel import VehicleBody
from Models.Vehicle.VehicleBrandModel import VehicleBrand
from Models.Vehicle.VehicleDriveModel import VehicleDrive
from Models.Vehicle.VehicleEngineTypeModel import VehicleEngineType
from Models.Vehicle.VehicleFuelModel import VehicleFuel
from Models.Vehicle.VehicleMakeModel import VehicleMake
from Models.Vehicle.VehicleModelModel import VehicleModel
from Models.Vehicle.VehicleShiftModel import VehicleShift

class AdminView20VehicleResource(Resource):
    """
    AdminView20VehicleResource is used by admins to see everything about the vehicle.
    Use HTTP GET method.
    Request must contain:
        access_token,
        upper_range 20.
    Request constrains:
        access_token must be linked to an existing admin in the database,
        upper_range must be lower than user count in the database,
        lower_range must be lower or equal to one.
    Responses:
        access_token is not linked to anyone:
            Response message: Your account can't be found.
            Response code: 404
        user does not have admin privilages:
            Response message: You don't have admin priviliges.
            Response code: 403
        upper_range is bigger than user count:
            Response message: upper_range is out of range.
            Response code: 417
        lower_range is equal or lower than zero:
            Response message: lower range is out of range.
            Response code: 417
        vehicle are not found:
            Response message: Vehicles are not found.
            Response code: 404
        vehicle are found:
            Response message: list<vehicle>
            Response code: 200
    """
    @jwt_required
    def get(self):
        upper_range = get_upperrange()
        lower_range = upper_range - 20

        current_user_id = get_jwt_identity()
        current_user = User.query.filter_by(user_id=current_user_id).first()
        if not current_user:
            return {"message": "Your account can't be found."}, 404
        admin_privalige = current_user.is_admin
        if not admin_privalige:
            return {"message": "You don't have admin priviliges."}, 403
        row_count = Vehicle.query.count()
        if upper_range > row_count:
            return {"message": "upper_range is out of range."}, 417
        if lower_range <= 0:
            return {"message": "lower range is out of range."}, 417
        vehicles = Vehicle.query.filter_by(Vehicle.vehicle_id.in_([lower_range, upper_range]))
        if not vehicles.first():
            return {"message": "Vehicles are not found."}, 404
        bodies = {}
        brands = {}
        drives = {}
        engineTypes = {}
        fuels = {}
        makes = {}
        models = {}
        shifts = {}
        for vehicle in vehicles:
            body = VehicleBody.query.filter_by(body_id=vehicle.body_id).first()
            brand = VehicleBrand.query.filter_by(brand_id=vehicle.brand_id).first()
            drive = VehicleDrive.query.filter_by(drive_id=vehicle.drive).first()
            engineType = VehicleEngineType.query.filter_by(engine_type_id=vehicle.engine_type_id).first()
            fuel = VehicleFuel.query.filter_by(fuel_id=vehicle.fuel_id).first()
            make = VehicleMake.query.filter_by(make_id=vehicle.make_id).first()
            model = VehicleModel.query.filter_by(model_id=vehicle.model_id).first()
            shift = VehicleShift.query.filter_by(shift_id=vehicle.shift_id).first()
            if body:
                bodies[vehicle.vehicle_id] = body.body_id
            if brand:
                brands[vehicle.vehicle_id] = brand.brand_id
            if drive:
                drives[vehicle.vehicle_id] = drive.drive_id
            if engineType:
                engineTypes[vehicle.vehicle_id] = engineType.engine_type_id
            if fuel:
                fuels[vehicle.vehicle_id] = fuel.fuel_id
            if make:
                makes[vehicle.vehicle_id] = make.make_id
            if model:
                models[vehicle.vehicle_id] = model.model_id
            if shift:
                shifts[vehicle.vehicle_id] = shift.shift_id
            
        data =  {
            "Vehicles": [vehicle.to_dict() for vehicle in vehicles.all()],
            "Vehicle Bodies": bodies,
            "Vehicle Brands": brands,
            "Vehicle Drives": drives,
            "Vehicle Engine Types": engineTypes,
            "Vehicle Fuels": fuels,
            "Vehicle Makes": makes,
            "Vehicle Models": models,
            "Vehicle Shifts": shifts
            }
        return data, 200
