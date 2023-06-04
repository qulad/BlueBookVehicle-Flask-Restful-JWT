from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from Resources.User import get_password1_password2, check_user_id, check_userid_password, delete_user_from_user_id
from Resources.Comment import view_all_comments_from_user_id, delete_comment_from_comment_id
from Resources.Vehicle import view_all_vehicles_from_user_id, delete_vehicle_from_vehicle_id
from Resources.Listing import view_all_listings_from_user_id, delete_listing_from_listing_id


class UserDeleteResource(Resource):
    """
    UserDeleteResource is used for deleting an existing user and everything related to the user.
    Use HTTP DELETE method.
    Request must contain:
        access_token,
        password1,
        password2,
    Request constrains:
        access_token must be linked to an existing user in the database.
        password1 and password2 must be same,
        password1 should be the same in the database.
    Responses:
        access_token is not linked to an existing user in the database:
            Response message: Your account can't be found.
            Response code: 404
        password1 and password2 are not same:
            Response message: Passwords must be the same.
            Response code: 400
        password is not the same in the database:
            Response message: Wrong password.
            Response code: 401
        user deleted:
            Response message: You have successfully deleted your account.
            Response code: 204
    """
    @jwt_required()
    def delete(self):
        password1, password2 = get_password1_password2()

        current_user_id = get_jwt_identity()
        error = check_user_id(current_user_id)
        if error:
            return error

        different_passwords = (password1 != password2)
        if different_passwords:
            return {"message": "Passwords must be the same."}, 400
        same_password = check_userid_password(user_id=current_user_id, password1=password1)
        if not same_password:
            return {"message": "Wrong password."}, 401
        
        vehicles = view_all_vehicles_from_user_id(current_user_id)
        if vehicles:
            for vehicle in vehicles:
                delete_vehicle_from_vehicle_id(vehicle.vehicle_id)
        comments = view_all_comments_from_user_id(current_user_id)
        if type(comments) == dict:
            for comment in comments.values():
                delete_comment_from_comment_id(comment.comment_id)
        listings = view_all_listings_from_user_id(current_user_id)
        if listings:
            for listing in listings:
                delete_listing_from_listing_id(listing.listing_id)
        delete_user_from_user_id(current_user_id)
        return {"message": "You have successfully deleted your account."}, 204
