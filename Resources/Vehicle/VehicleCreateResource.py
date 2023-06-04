from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from Resources.User import check_user_id
from Resources.Vehicle import get_all_args, check_body_id, check_brand_id, check_drive_id, check_engine_type_id, check_fuel_id, check_make_id, check_model_id, check_shift_id, check_type_id, add_vehicle


class VehicleCreateResource(Resource):
    """
    VehicleCreateResource is used for adding a new row to Vehicle model.
    Use HTTP POST method.
    Request must contain:
        access_token,
        vehicle_image_url,
        type_id,
        brand_id,
        model_id,
        make_id,
        fuel_id,
        engine_type_id,
        price,
        title,
        description,
        thousand_km,
        tork,
        battery_capacity,
        range_km,
        charge_time,
        charge_watt,
        shift_id,
        used,
        drive_id,
        door_count,
        seat_count,
        body_id,
        engine_volume,
        parking_sensor,
        glass_rooftop,
        central_console,
        folding_mirror.
    Request constrains:
        access_token must be linked to an existing user,
        type_id must be in the VehicleType table,
        brand_id must be in the VehicleBrand table,
        model_id must be in the VehicleModel table,
        make_id must be in the VehicleMake table,
        fuel_id must be in the VehicleFuel table,
        engine_type_id must be in the VehicleEngineType table,
        battery_capacity must be present if EV.
        range_km must be present if EV.
        charge_time must be present if EV.
        charge_watt must be present if EV.
        shift_id must be in the VehicleShiftTable,
        drive_id must be in the VehicleDriveTable,
        body_id must be in the VehicleBodyTable.
    Responses:
        access_token is not linked to an existing user:
            Response message: Your account can't be found.
            Response code: 404
        brand_id is not in the VehicleBrand table:
            Response message: Can't find the brand.
            Response code: 404
        model_id is not in the VehicleModel table:
            Response message: Can't find the model.
            Response code: 404
        make_id is not in the VehicleMake table:
            Response message: Can't find the make.
            Response code: 404
        fuel_id is not in the VehicleFuel table:
            Response message: Can't find the fuel.
            Response code: 404
        engine_type_id is not in the VehicleEngineType table:
            Response message: Can't find the engine type.
            Response code: 404
        battery_capacity is not present if EV:
            Response message: Can't find the battery capacity.
            Response code: 404
        range_km is not present if EV:
            Response message: Can't find the range.
            Response code: 404
        charge_time is not present if EV:
            Response message: Can't find the charge time.
            Response code: 404
        charge_watt is not present if EV:
            Response message: Can't find the charge watt.
            Response code: 404
        shift_id is not in the VehicleShiftTable:
            Response message: Can't find the shift.
            Response code: 404
        drive_id is not in the VehicleDriveTable:
            Response message: Can't find the drive.
            Response code: 404
        body_id is not in the VehicleBodyTable:
            Response message: Can't find the body.
            Response code: 404
        vehicle added:
            Response message: <vehicle_id>
            Response code: 201
    """
    @jwt_required
    def post(self):
        args = get_all_args()

        battery_capacity = None
        range_km = None
        charge_time = None
        charge_watt = None

        current_user_id = get_jwt_identity()
        current_user = check_user_id(current_user_id)
        if not current_user:
            return current_user
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
        
        vehicle_id = add_vehicle(
            vehicle_image_url = args["vehicle_image_url"],
            type_id = args["type_id"],
            brand_id = args["brand_id"],
            model_id = args["model_id"],
            make_id = args["make_id"],
            fuel_id = args["fuel_id"],
            user_id = current_user.user_id,
            engine_type_id = args["engine_type_id"],
            price = args["price"],
            title = args["title"],
            description = args["description"],
            thousand_km = args["thousand_km"],
            tork = args["tork"],
            shift_id = args["shift_id"],
            used = args["used"],
            drive_id = args["drive_id"],
            door_count = args["door_count"],
            seat_count = args["seat_count"],
            body_id = args["body_id"],
            engine_volume = args["engine_volume"],
            parking_sensor = args["parking_sensor"],
            glass_rooftop = args["glass_rooftop"],
            central_console = args["central_console"],
            folding_mirror = args["folding_mirror"],
            battery_capacity = battery_capacity,
            range_km = range_km,
            charge_time = charge_time,
            charge_watt = charge_watt
        )
        return {"vehicle_id": vehicle_id}, 201
        