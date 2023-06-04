from flask_restful import reqparse
from Models.Vehicle.VehicleBodyModel import VehicleBody
from Models.Vehicle.VehicleBrandModel import VehicleBrand
from Models.Vehicle.VehicleDriveModel import VehicleDrive
from Models.Vehicle.VehicleEngineTypeModel import VehicleEngineType
from Models.Vehicle.VehicleFuelModel import VehicleFuel
from Models.Vehicle.VehicleMakeModel import VehicleMake
from Models.Vehicle.VehicleModelModel import VehicleModel
from Models.Vehicle.VehicleShiftModel import VehicleShift

def get_listingid():
    parser = reqparse.RequestParser()
    parser.add_argument("listing_id", type=int, required=True)
    args = parser.parse_args()
    return args["listing_id"]
    
def get_commentid():
    parser = reqparse.RequestParser()
    parser.add_argument("comment_id", type=int, required=True)
    args = parser.parse_args()
    return args["comment_id"]

def get_tablename_rowname_brandid_modelid():
    parser = reqparse.RequestParser()
    parser.add_argument("table_name", type=str, required=True)
    parser.add_argument("row_name", type=str, required=True)
    parser.add_argument("brand_id", type=int, required=False)
    parser.add_argument("model_id", type=int, required=False)
    args = parser.parse_args()
    return args["table_name"], args["row_name"], args["brand_id"], args["model_id"]

def get_table_from_str(table_name):
    if table_name == "VehicleBody":
        return VehicleBody
    elif table_name == "VehicleBrand":
        return VehicleBrand
    elif table_name == "VehicleDrive":
        return VehicleDrive
    elif table_name == "VehicleEngineType":
        return VehicleEngineType
    elif table_name == "VehicleFuel":
        return VehicleFuel
    elif table_name == "VehicleMake":
        return VehicleMake
    elif table_name == "VehicleModel":
        return VehicleModel
    elif table_name == "VehicleShift":
        return VehicleShift
    return -1

def get_upperrange():
    parser = reqparse.RequestParser()
    parser.add_argument("upper_range")
    args = parser.parse_args()
    if args["upper_range"] == None:
        args["upper_range"] = 20
    return args["upper_range"]
