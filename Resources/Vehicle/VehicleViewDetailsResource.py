from flask_restful import Resource
from Resources.Vehicle import get_vehicleid
from Resources.Vehicle import check_body_id, check_brand_id, check_drive_id, check_engine_type_id, check_fuel_id, check_make_id, check_model_id, check_shift_id, check_type_id, view_vehicle_from_vehicle_id

class VehicleViewDetailsResource(Resource):
    """
    VehicleViewDetailsResource is used for getting vehicle details from vehicle_id.
    Use HTTP GET method.
    Request must contain:
        vehicle_id.
    Request constrains:
        vehicle_id must be linked to an existing vehicle in the database.
    Responses:
        vehicle_id is not linked to an existing vehicle in the database:
            Response message: Vehicle can't be found.
            Response code: 404
        type_id is not linked to an existing vehicle int the database:
            Response message: Vehicle component can't be found.
            Response code: 404
        brand_id is not linked to an existing vehicle in the database:
            Response message: Vehicle component can't be found.
            Response code: 404
        model_id is not linked to an existing vehicle in the database:
            Response message: Vehicle component can't be found.
            Response code: 404
        make_id is not linked to an existing vehicle in the database:
            Response message: Vehicle component can't be found.
            Response code: 404
        fuel_id is not linked to an existing vehicle in the database:
            Response message: Vehicle component can't be found.
            Response code: 404
        user_id is not linked to an existing vehicle in the database:
            Response message: Vehicle component can't be found.
            Response code: 404
        engine_type_id is not linked to an existing vehicle in the database:
            Response message: Vehicle component can't be found.
            Response code: 404
        shift_id is not linked to an existing vehicle in the database:
            Response message: Vehicle component can't be found.
            Response code: 404
        drive_id is not linked to an existing vehicle in the database:
            Response message: Vehicle component can't be found.
            Response code: 404
        body_id is not linked to an existing vehicle in the database:
            Response message: Vehicle component can't be found.
            Response code: 404
        vehicle is found:
            Response message: dict<vehicle>
            Response code: 200
        if engine_type is 'Electric', battery_capacity, range_km, charge_time, charge_watt must not be None:
            Response message: Vehicle component can't be found.
            Reponse code: 404
    """
    def get(self):
        vehicle_id = get_vehicleid()

        args = view_vehicle_from_vehicle_id(vehicle_id)
        type_ = check_type_id(args["type_id"])
        if not type_:
            return type_
        brand = check_brand_id(args["brand_id"])
        if not brand:
            return brand
        model = check_model_id(model_id=args["model_id"], brand_id=args["brand_id"])
        if not model:
            return model
        make = check_make_id(model_id=args["model_id"], make_id=args["make_id"])
        if not make:
            return make
        fuel = check_fuel_id(args["fuel_id"])
        if not fuel:
            return fuel
        engine_type = check_engine_type_id(args["engine_type_id"])
        if not engine_type:
            return engine_type
        if engine_type.engine_type == "Electric":
            battery_capacity = args.get("battery_capacity")
            if battery_capacity == None:
                return {"message": "Can't find the battery capacity."}, 404
            range_km = args.get("range_km")
            if range_km == None:
                return {"message": "Can't find the range."}, 404
            charge_time = args.get("charge_time")
            if charge_time == None:
                return {"message": "Can't find the charge time."}, 404
            charge_watt = args.get("charge_watt")
            if charge_watt == None:
                return {"message": "Can't find the charge watt."}, 404
        shift = check_shift_id(args["shift_id"])
        if not shift:
            return shift
        drive = check_drive_id(args["drive_id"])
        if not drive:
            return drive
        body = check_body_id(args["body_id"])
        if not body:
            return body
        return args, 200
