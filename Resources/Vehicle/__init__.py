from sqlalchemy import func
from flask_restful import reqparse
from Models import db
from Models.Listing.ListingModel import Listing
from Models.Vehicle.VehicleModel import Vehicle
from Models.Vehicle.VehicleBodyModel import VehicleBody
from Models.Vehicle.VehicleTypeModel import VehicleType
from Models.Vehicle.VehicleFuelModel import VehicleFuel
from Models.Vehicle.VehicleMakeModel import VehicleMake
from Models.Vehicle.VehicleBrandModel import VehicleBrand
from Models.Vehicle.VehicleDriveModel import VehicleDrive
from Models.Vehicle.VehicleModelModel import VehicleModel
from Models.Vehicle.VehicleShiftModel import VehicleShift
from Models.Vehicle.VehicleEngineTypeModel import VehicleEngineType


def get_all_args():
    parser = reqparse.RequestParser()
    parser.parse_args("vehicle_image_url", type=str, required=True)
    parser.parse_args("type_id", type=int, required=True)
    parser.parse_args("brand_id", type=int, required=True)
    parser.parse_args("model_id", type=int, required=True)
    parser.parse_args("make_id", type=int, required=True)
    parser.parse_args("fuel_id", type=int, required=True)
    parser.parse_args("engine_type_id", type=int, required=True)
    parser.parse_args("price", type=float, required=True)
    parser.parse_args("title", type=str, required=True)
    parser.parse_args("description", type=str, required=True)
    parser.parse_args("thousand_km", type=int, required=True)
    parser.parse_args("tork", type=float, required=True)
    parser.parse_args("battery_capacity", type=float, required=False)
    parser.parse_args("range_km", type=int, required=False)
    parser.parse_args("charge_time", type=int, required=False)
    parser.parse_args("charge_watt", type=int, required=False)
    parser.parse_args("shift_id", type=int, required=True)
    parser.parse_args("used", type=bool, required=True)
    parser.parse_args("drive_id", type=int, required=True)
    parser.parse_args("door_count", type=int, required=True)
    parser.parse_args("seat_count", type=int, required=True)
    parser.parse_args("body_id", type=int, required=True)
    parser.parse_args("engine_volume", type=bool, required=True)
    parser.parse_args("parking_sensor", type=bool, required=True)
    parser.parse_args("glass_rooftop", type=bool, required=True)
    parser.parse_args("central_console", type=bool, required=True)
    parser.parse_args("folding_mirror", type=bool, required=True)
    args = parser.parse_args()
    return args

def get_vehicleid():
    parser = reqparse.RequestParser()
    parser.parse_args("vehicle_id", type=int, required=True)
    args = parser.parse_args()
    return args["vehicle_id"]

def check_vehicle_id(vehicle_id):
    vehicle_id_valid = Vehicle.query.filter_by(vehicle_id=vehicle_id).first()
    if not vehicle_id_valid:
        return {"message": "Vehicle can't be found."}, 404
    
def check_type_id(type_id):
    type_id_valid = VehicleType.query.filter_by(type_id=type_id).first()
    if not type_id_valid:
        return {"message": "Vehicle type can't be found."}, 404

def check_brand_id(brand_id):
    brand_id_valid = VehicleBrand.query.filter_by(brand_id=brand_id).first()
    if not brand_id_valid:
        return {"message": "Vehicle brand can't be found."}, 404

def check_model_id(model_id, brand_id):
    model_id_valid = VehicleModel.query.filter_by(model_id=model_id, brand_id=brand_id).first()
    if not model_id_valid:
        return {"message": "Vehicle model can't be found."}, 404

def check_make_id(make_id, model_id):
    make_id_valid = VehicleMake.query.filter_by(make_id=make_id, model_id=model_id).first()
    if not make_id_valid:
        return {"message": "Vehicle make can't be found."}, 404

def check_fuel_id(fuel_id):
    fuel_id_valid = VehicleFuel.query.filter_by(fuel_id=fuel_id).first()
    if not fuel_id_valid:
        return {"message": "Vehicle fuel can't be found."}, 404

def check_engine_type_id(engine_type_id):
    engine_type_id_valid = VehicleEngineType.query.filter_by(engine_type_id=engine_type_id).first()
    if not engine_type_id_valid:
        return {"message": "Vehicle engine type can't be found."}, 404

def check_shift_id(shift_id):
    shift_id_valid = VehicleShift.query.filter_by(shift_id=shift_id).first()
    if not shift_id_valid:
        return {"message": "Vehicle shift can't be found."}, 404

def check_drive_id(drive_id):
    drive_id_valid = VehicleDrive.query.filter_by(drive_id=drive_id).first()
    if not drive_id_valid:
        return {"message": "Vehicle drive can't be found."}, 404

def check_body_id(body_id):
    body_id_valid = VehicleBody.query.filter_by(body_id=body_id).first()
    if not body_id_valid:
        return {"message": "Vehicle body can't be found."}, 404

def check_vehicle_upper_range(upper_range):
    row_count = Vehicle.query.count()
    if upper_range > row_count:
        return {"message": "upper_range is out of range."}, 417

def check_user_owns_vehicle(user_id, vehicle_id):
    vehicle = Vehicle.query.filter_by(vehicle_id=vehicle_id).first()
    same_user = (vehicle.user_id == user_id)
    if not same_user:
        return {"message": "This is not your vehicle."}, 403

def view_all_vehicles_from_user_id(user_id):
    vehicles = Vehicle.query.filter_by(user_id=user_id)
    if vehicles.first():
        vehicles = list(vehicles.all())
        return vehicles

def view_vehicle_from_vehicle_id(vehicle_id):
    vehicle = Vehicle.query.filter_by(vehicle_id=vehicle_id).first()
    vehicle_body = VehicleBody.query.filter_by(body_id=vehicle.body_id).first()
    vehicle_brand = VehicleBrand.query.filter_by(brand_id=vehicle.brand_id).first()
    vehicle_drive = VehicleDrive.query.filter_by(drive_id=vehicle.drive_id).first()
    vehicle_engine_type = VehicleEngineType.query.filter_by(engine_type_id=vehicle.engine_type_id).first()
    vehicle_fuel = VehicleFuel.query.filter_by(fuel_id=vehicle.fuel_id).first()
    vehicle_make = VehicleMake.query.filter_by(make_id=vehicle.make_id).first()
    vehicle_model = VehicleModel.query.filter_by(model_id=vehicle.model_id).first()
    vehicle_shift = VehicleShift.query.filter_by(shift_id=vehicle.shift_id).first()
    vehicle_type = VehicleType.query.filter_by(type_id=vehicle.type_id).first()
    data = {
        "vehicle_id": vehicle.vehicle_id,
        "vehicle_image_url": vehicle.vehicle_image_url,
        "vehicle_type": vehicle_type.vehicle_type,
        "vehicle_brand": vehicle_brand.brand_type,
        "vehicle_model": vehicle_model.model_type,
        "vehicle_make": vehicle_make.make_year,
        "vehicle_fuel": vehicle_fuel.fuel_type,
        "original_poster_id": vehicle.user_id,
        "vehicle_engine_type_id": vehicle_engine_type.engine_type,
        "vehicle_price": vehicle.price,
        "vehicle_title": vehicle.title,
        "vehicle_description": vehicle.description,
        "vehicle_thousand_km": vehicle.thousand_km,
        "vehicle_tork": vehicle.tork,
        "vehicle_battery_capacity": vehicle.battery_capacity,
        "vehicle_range_km": vehicle.range_km,
        "vehicle_charge_time": vehicle.charge_time,
        "vehicle_charge_watt": vehicle.charge_watt,
        "vehhicle_shift": vehicle_shift.shift_type,
        "vehicle_used": vehicle.used,
        "vehicle_drive": vehicle_drive.shift_type,
        "vehicle_door_count": vehicle.door_count,
        "vehicle_seat_count": vehicle.seat_count,
        "vehicle_body": vehicle_body.body_type,
        "vehicle_engine_volume": vehicle.engine_volume,
        "vehicle_parking_sensor": vehicle.parking_sensor,
        "vehicle_glass_rooftop": vehicle.glass_rooftop,
        "vehicle_central_console": vehicle.central_console,
        "vehicle_folding_mirror": vehicle.folding_mirror
    }
    return data

def view_vehicle_from_user_id(user_id):
    vehicle = Vehicle.query.filter_by(vehicle_id=user_id).first()
    vehicle_body = VehicleBody.query.filter_by(body_id=vehicle.body_id).first()
    vehicle_brand = VehicleBrand.query.filter_by(brand_id=vehicle.brand_id).first()
    vehicle_drive = VehicleDrive.query.filter_by(drive_id=vehicle.drive_id).first()
    vehicle_engine_type = VehicleEngineType.query.filter_by(engine_type_id=vehicle.engine_type_id).first()
    vehicle_fuel = VehicleFuel.query.filter_by(fuel_id=vehicle.fuel_id).first()
    vehicle_make = VehicleMake.query.filter_by(make_id=vehicle.make_id).first()
    vehicle_model = VehicleModel.query.filter_by(model_id=vehicle.model_id).first()
    vehicle_shift = VehicleShift.query.filter_by(shift_id=vehicle.shift_id).first()
    vehicle_type = VehicleType.query.filter_by(type_id=vehicle.type_id).first()
    data = {
        "vehicle_id": vehicle.vehicle_id,
        "vehicle_image_url": vehicle.vehicle_image_url,
        "vehicle_type": vehicle_type.vehicle_type,
        "vehicle_brand": vehicle_brand.brand_type,
        "vehicle_model": vehicle_model.model_type,
        "vehicle_make": vehicle_make.make_year,
        "vehicle_fuel": vehicle_fuel.fuel_type,
        "original_poster_id": vehicle.user_id,
        "vehicle_engine_type_id": vehicle_engine_type.engine_type,
        "vehicle_price": vehicle.price,
        "vehicle_title": vehicle.title,
        "vehicle_description": vehicle.description,
        "vehicle_thousand_km": vehicle.thousand_km,
        "vehicle_tork": vehicle.tork,
        "vehicle_battery_capacity": vehicle.battery_capacity,
        "vehicle_range_km": vehicle.range_km,
        "vehicle_charge_time": vehicle.charge_time,
        "vehicle_charge_watt": vehicle.charge_watt,
        "vehhicle_shift": vehicle_shift.shift_type,
        "vehicle_used": vehicle.used,
        "vehicle_drive": vehicle_drive.shift_type,
        "vehicle_door_count": vehicle.door_count,
        "vehicle_seat_count": vehicle.seat_count,
        "vehicle_body": vehicle_body.body_type,
        "vehicle_engine_volume": vehicle.engine_volume,
        "vehicle_parking_sensor": vehicle.parking_sensor,
        "vehicle_glass_rooftop": vehicle.glass_rooftop,
        "vehicle_central_console": vehicle.central_console,
        "vehicle_folding_mirror": vehicle.folding_mirror
    }
    return data

def view_random_vehicle_within_range(range):
    vehicles = Vehicle.query.order_by(func.random()).limit(range).all()
    vehicles = list(vehicles)
    output = {}
    for i in range(range):
        vehicle = vehicles[i]
        vehicle_body = VehicleBody.query.filter_by(body_id=vehicle.body_id).first()
        vehicle_brand = VehicleBrand.query.filter_by(brand_id=vehicle.brand_id).first()
        vehicle_drive = VehicleDrive.query.filter_by(drive_id=vehicle.drive_id).first()
        vehicle_engine_type = VehicleEngineType.query.filter_by(engine_type_id=vehicle.engine_type_id).first()
        vehicle_fuel = VehicleFuel.query.filter_by(fuel_id=vehicle.fuel_id).first()
        vehicle_make = VehicleMake.query.filter_by(make_id=vehicle.make_id).first()
        vehicle_model = VehicleModel.query.filter_by(model_id=vehicle.model_id).first()
        vehicle_shift = VehicleShift.query.filter_by(shift_id=vehicle.shift_id).first()
        vehicle_type = VehicleType.query.filter_by(type_id=vehicle.type_id).first()
        data = {
            "vehicle_id": vehicle.vehicle_id,
            "vehicle_image_url": vehicle.vehicle_image_url,
            "vehicle_type": vehicle_type.vehicle_type,
            "vehicle_brand": vehicle_brand.brand_type,
            "vehicle_model": vehicle_model.model_type,
            "vehicle_make": vehicle_make.make_year,
            "vehicle_fuel": vehicle_fuel.fuel_type,
            "original_poster_id": vehicle.user_id,
            "vehicle_engine_type_id": vehicle_engine_type.engine_type,
            "vehicle_price": vehicle.price,
            "vehicle_title": vehicle.title,
            "vehicle_description": vehicle.description,
            "vehicle_thousand_km": vehicle.thousand_km,
            "vehicle_tork": vehicle.tork,
            "vehicle_battery_capacity": vehicle.battery_capacity,
            "vehicle_range_km": vehicle.range_km,
            "vehicle_charge_time": vehicle.charge_time,
            "vehicle_charge_watt": vehicle.charge_watt,
            "vehhicle_shift": vehicle_shift.shift_type,
            "vehicle_used": vehicle.used,
            "vehicle_drive": vehicle_drive.shift_type,
            "vehicle_door_count": vehicle.door_count,
            "vehicle_seat_count": vehicle.seat_count,
            "vehicle_body": vehicle_body.body_type,
            "vehicle_engine_volume": vehicle.engine_volume,
            "vehicle_parking_sensor": vehicle.parking_sensor,
            "vehicle_glass_rooftop": vehicle.glass_rooftop,
            "vehicle_central_console": vehicle.central_console,
            "vehicle_folding_mirror": vehicle.folding_mirror
        }
        output[f"vehicle {i}"] = data
    return output

def view_vehicle_from_listing_id(listing_id):
    listing = Listing.query.filter_by(listing_id=listing_id).first()
    vehicle = Vehicle.query.filter_by(vehicle_id=listing.vehicle_id).first()
    vehicle_body = VehicleBody.query.filter_by(body_id=vehicle.body_id).first()
    vehicle_brand = VehicleBrand.query.filter_by(brand_id=vehicle.brand_id).first()
    vehicle_drive = VehicleDrive.query.filter_by(drive_id=vehicle.drive_id).first()
    vehicle_engine_type = VehicleEngineType.query.filter_by(engine_type_id=vehicle.engine_type_id).first()
    vehicle_fuel = VehicleFuel.query.filter_by(fuel_id=vehicle.fuel_id).first()
    vehicle_make = VehicleMake.query.filter_by(make_id=vehicle.make_id).first()
    vehicle_model = VehicleModel.query.filter_by(model_id=vehicle.model_id).first()
    vehicle_shift = VehicleShift.query.filter_by(shift_id=vehicle.shift_id).first()
    vehicle_type = VehicleType.query.filter_by(type_id=vehicle.type_id).first()
    data = {
        "vehicle_id": vehicle.vehicle_id,
        "vehicle_image_url": vehicle.vehicle_image_url,
        "vehicle_type": vehicle_type.vehicle_type,
        "vehicle_brand": vehicle_brand.brand_type,
        "vehicle_model": vehicle_model.model_type,
        "vehicle_make": vehicle_make.make_year,
        "vehicle_fuel": vehicle_fuel.fuel_type,
        "original_poster_id": vehicle.user_id,
        "vehicle_engine_type_id": vehicle_engine_type.engine_type,
        "vehicle_price": vehicle.price,
        "vehicle_title": vehicle.title,
        "vehicle_description": vehicle.description,
        "vehicle_thousand_km": vehicle.thousand_km,
        "vehicle_tork": vehicle.tork,
        "vehicle_battery_capacity": vehicle.battery_capacity,
        "vehicle_range_km": vehicle.range_km,
        "vehicle_charge_time": vehicle.charge_time,
        "vehicle_charge_watt": vehicle.charge_watt,
        "vehhicle_shift": vehicle_shift.shift_type,
        "vehicle_used": vehicle.used,
        "vehicle_drive": vehicle_drive.shift_type,
        "vehicle_door_count": vehicle.door_count,
        "vehicle_seat_count": vehicle.seat_count,
        "vehicle_body": vehicle_body.body_type,
        "vehicle_engine_volume": vehicle.engine_volume,
        "vehicle_parking_sensor": vehicle.parking_sensor,
        "vehicle_glass_rooftop": vehicle.glass_rooftop,
        "vehicle_central_console": vehicle.central_console,
        "vehicle_folding_mirror": vehicle.folding_mirror
    }
    return data

def add_vehicle(type_id, brand_id, model_id, make_id, fuel_id, user_id, engine_type_id, price, title, description, thousand_km, tork, battery_capacity, range_km, charge_time, charge_watt, shift_id, used, drive_id, door_count, seat_count, body_id, engine_volume, parking_sensor, glass_rooftop, central_console, folding_mirror, vehicle_image_url):
    new_vehicle = Vehicle(
        vehicle_image_url=vehicle_image_url,
        type_id=type_id,
        brand_id=brand_id,
        model_id=model_id,
        make_id=make_id,
        fuel_id=fuel_id,
        user_id=user_id,
        engine_type_id=engine_type_id,
        price=price,
        title=title,
        description=description,
        thousand_km=thousand_km,
        tork=tork,
        battery_capacity=battery_capacity,
        range_km=range_km,
        charge_time=charge_time,
        charge_watt=charge_watt,
        shift_id=shift_id,
        used=used,
        drive_id=drive_id,
        door_count=door_count,
        seat_count=seat_count,
        body_id=body_id,
        engine_volume=engine_volume,
        parking_sensor=parking_sensor,
        glass_rooftop=glass_rooftop,
        central_console=central_console,
        folding_mirror=folding_mirror
    )
    db.session.add(new_vehicle)
    db.session.commit()
    return new_vehicle.vehicle_id

def delete_vehicle_from_vehicle_id(vehicle_id):
    vehicle = Vehicle.query.filter_by(vehicle_id=vehicle_id).first()
    db.session.delete(vehicle)
    db.session.commit()

def search_with_query(search_query):
    results = Vehicle.query.filter_by(**search_query).all()
    output = {}
    for i in range(len(list(results))):
        output[f"vehicle_id_{i}"] = list(results)[i].vehicle_id
    return output
