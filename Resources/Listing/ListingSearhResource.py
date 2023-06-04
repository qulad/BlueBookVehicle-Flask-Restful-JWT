from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity
from Resources.User import check_user_id
from Resources.Listing import get_listing_id_from_vehicle_id, get_all_search_args, get_listing_details_from_listing_id, view_listing_detail_from_listing_id
from Resources.Vehicle import search_with_query

class ListingSearchResource(Resource):
    """
    ListingSearchResource is used for searching rows from Listing Table.
    Use HTTP Get Method.
    Request must contain:
        vehicle_args
    Request constrains:
    Responses:
    """
    def get(self):
        args = get_all_search_args()

        search_query = {}
        for key in args:
            if args.get(key) != None:
                search_query[key] = args.get(key)
        vehicle_ids = search_with_query(search_query)
        listing_ids = []
        for vehicle_id in vehicle_ids:
            listing_ids.append(get_listing_id_from_vehicle_id(vehicle_id))
        output = {}
        for i in range(len(listing_ids)):
            listing_id = listing_ids[i]

            listing = get_listing_details_from_listing_id(listing_id)
            error = check_user_id(listing.user_id)
            if error:
                continue
            if listing.listing_active:
                data = view_listing_detail_from_listing_id(listing_id)
                output[f"result_{i}"] = data
            else:
                current_user = get_jwt_identity()
                if not current_user:
                    continue
                else:
                    same_user = (current_user == listing)
                    if not same_user:
                        continue
                    else:
                        data = view_listing_detail_from_listing_id(listing_id)
                        output[f"result_{i}"] = data
