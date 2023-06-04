from sqlalchemy import func, or_
from flask_restful import reqparse
from Models import db
from Models.Listing.ListingModel import Listing
from Resources.User import check_user_id, view_user_from_user_id
from Resources.Vehicle import check_vehicle_id, view_vehicle_from_vehicle_id, add_vehicle

def get_listingid():
    parser = reqparse.RequestParser()
    parser.add_argument("listing_id", type=int, required=True)
    args = parser.parse_args()
    return args["listing_id"]

def get_range():
    parser = reqparse.RequestParser()
    parser.add_argument("range", type=int, required=True)
    args = parser.parse_args()
    return args["range"] 

def get_vehicle_id():
    parser = reqparse.RequestParser()
    parser.add_argument("vehicle_id", type=int, required=True)
    args = parser.parse_args()
    return args["vehicle_id"] 

def get_listingid_vehicleid():
    parser = reqparse.RequestParser()
    parser.add_argument("listing_id", type=int, required=True)
    parser.add_argument("vehicle_id", type=int, required=True)
    args = parser.parse_args()
    return args["listing_id"], args["vehicle_id"]

def get_all_search_args():
    parser = reqparse.RequestParser()
    parser.parse_args("vehicle_image_url", type=str, required=False)
    parser.parse_args("type_id", type=int, required=False)
    parser.parse_args("brand_id", type=int, required=False)
    parser.parse_args("model_id", type=int, required=False)
    parser.parse_args("make_id", type=int, required=False)
    parser.parse_args("fuel_id", type=int, required=False)
    parser.parse_args("engine_type_id", type=int, required=False)
    parser.parse_args("price", type=float, required=False)
    parser.parse_args("title", type=str, required=False)
    parser.parse_args("description", type=str, required=False)
    parser.parse_args("thousand_km", type=int, required=False)
    parser.parse_args("tork", type=float, required=False)
    parser.parse_args("battery_capacity", type=float, required=False)
    parser.parse_args("range_km", type=int, required=False)
    parser.parse_args("charge_time", type=int, required=False)
    parser.parse_args("charge_watt", type=int, required=False)
    parser.parse_args("shift_id", type=int, required=False)
    parser.parse_args("used", type=bool, required=False)
    parser.parse_args("drive_id", type=int, required=False)
    parser.parse_args("door_count", type=int, required=False)
    parser.parse_args("seat_count", type=int, required=False)
    parser.parse_args("body_id", type=int, required=False)
    parser.parse_args("engine_volume", type=bool, required=False)
    parser.parse_args("parking_sensor", type=bool, required=False)
    parser.parse_args("glass_rooftop", type=bool, required=False)
    parser.parse_args("central_console", type=bool, required=False)
    parser.parse_args("folding_mirror", type=bool, required=False)
    args = parser.parse_args()
    return args

def get_listing_id_from_vehicle_id(vehicle_id):
    return Listing.query.filter_by(vehicle_id=vehicle_id).first().listing_id

def get_listing_details_from_listing_id(listing_id):
    return Listing.query.filter_by(listing_id=listing_id).first()

def check_listing_id(listing_id):
    listing_id_valid = Listing.query.filter_by(listing_id=listing_id).first()
    if not listing_id_valid:
        return {"message": "Listing can't be found."}, 404

def check_listing_active(listing_id) -> bool:
    listing = Listing.query.filter_by(listing_id=listing_id).first()
    listing_active = listing.listing_active
    return listing_active

def check_listing_waiting_for_new_approval(listing_id):
    listing = Listing.query.filter_by(listing_id=listing_id).first()
    listing_new_waiting = listing.new_waiting
    return listing_new_waiting

def check_listing_waiting_for_edit_approval(listing_id):
    listing = Listing.query.filter_by(listing_id=listing_id).first()
    listing_edit_waiting = listing.edit_waiting
    return listing_edit_waiting

def check_listing_upper_range(upper_range):
    row_count = Listing.query.count()
    if upper_range > row_count:
        return {"message": "upper_range is out of range."}, 417

def view_all_listings_from_user_id(user_id):
    listings = Listing.query.filter_by(user_id)
    if listings.first():
        listings = list(listings.all())
        return listings

def view_listing_detail_from_listing_id(listing_id):
    listing = Listing.query.filter_by(listing_id=listing_id)
    data = {
        "listing_id": listing.listing_id,
        "user": view_user_from_user_id(listing.user_id),
        "vehicle": view_vehicle_from_vehicle_id(listing.vehicle_id),
        "edited": listing.edited,
        "listing_active": listing.listing_active
    }
    return data

def view_listing_preview_from_user_id_within_range(user_id, lower_range, upper_range):
    listings = Listing.query.filter_by(user_id=user_id, listing_active=True)
    if not listing.first():
        return {"message": "There are no listings."}, 404
    listings = list(listings.all())[(lower_range-1):upper_range]
    output = {}
    for i in range(range):
        listing = listings[i]
        if not listing:
            break
        vehicle = view_vehicle_from_vehicle_id(listing.vehicle_id)
        user = view_user_from_user_id(listing.user_id)
        data = {
            "listing_id": listing.listing_id,
            "vehicle": {
                "title": vehicle.title,
                "vehicle_image_url": vehicle.vehicle_image_url
            },
            "user": {
                "user_name": user.user_name,
                "profile_image_url": user.profile_image_url
            }
        }
        output[f"vehicle {i}"] = data
    return output

def view_random_listing_preview_within_range(user_id, range):
    listings = Listing.query.filter_by(or_(Listing.listing_active==True, Listing.user_i==user_id)).order_by(func.random(range))
    if not listing.first():
        return {"message": "There are no listings."}, 404
    listings = list(listings.all())
    output = {}
    for i in range(range):
        listing = listings[i]
        if not listing:
            break
        valid = check_vehicle_id(listing.vehicle_id)
        if not valid:
            continue
        valid = check_user_id(listing.user_id)
        if not valid:
            continue
        vehicle = view_vehicle_from_vehicle_id(listing.vehicle_id)
        user = view_user_from_user_id(listing.user_id)
        data = {
            "listing_id": listing.listing_id,
            "vehicle": {
                "title": vehicle.title,
                "vehicle_image_url": vehicle.vehicle_image_url
            },
            "user": {
                "user_name": user.user_name,
                "profile_image_url": user.profile_image_url
            }
        }
        output[f"vehicle {i}"] = data
    return output

def add_listing(user_id, vehicle_id):
    new_listing = Listing(user_id=user_id, vehicle_id=vehicle_id)
    db.session.add(new_listing)
    db.session.commit()
    return new_listing.listing_id

def edit_listing_from_listing_id(listing_id, new_vehicle_id):
    listing = Listing.query.filter_by(listing_id=listing_id).first()
    listing.new_vehicle_id = new_vehicle_id
    listing.edit_waiting = True
    db.session.commit()
    return listing.listing_id

def edit_listing_list(listing_id):
    listing = Listing.query.filter_by(listing_id=listing_id).first()
    listing.listing_activate = True
    db.session.commit()

def edit_listing_unlist(listing_id):
    listing = Listing.query.filter_by(listing_id=listing_id).first()
    listing.listing_activate = False
    db.session.commit()

def delete_listing_from_listing_id(listing_id):
    listing = Listing.query.filter_by(listing_id=listing_id).first()
    db.session.delete(listing)
    db.session.commit()
    