from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity
from Resources.Listing import get_range, view_random_listing_preview_within_range

class ListingViewRandomRangePreviewResource(Resource):
    """
    ListingViewRandomRangePreviewResource is used for viewing a random row from Listing Table.
    Use HTTP Get Method.
    Request must contain:
        range.
    Request constrains:
        range must be lower than Listing table's row count.
    Responses:
        listings:
            Response Message: dict<listings>
            Response Code: 200
    """
    def get(self):
        range = get_range()
        current_user_id = get_jwt_identity()
        data = view_random_listing_preview_within_range(user_id=current_user_id, range=range)
        return data, 200
