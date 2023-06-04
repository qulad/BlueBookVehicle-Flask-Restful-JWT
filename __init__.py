from Resources.Admin.AdminAcceptPendingEditListingResource import AdminAcceptPendingEditListingResource
from Resources.Admin.AdminAcceptPendingNewListingResource import AdminAcceptPendingNewListingResource
from Resources.Admin.AdminAddNewRowToTableResource import AdminAddNewRowToTableResource
from Resources.Admin.AdminDeleteCommentResource import AdminDeleteCommentResource
from Resources.Admin.AdminDenyPendingEditListingResource import AdminDenyPendingEditListingResource
from Resources.Admin.AdminDenyPendingNewListingResource import AdminDenyPendingNewListingResource
from Resources.Admin.AdminView20CommentResource import AdminView20CommentResource
from Resources.Admin.AdminView20ListingResource import AdminView20ListingResource
from Resources.Admin.AdminView20UsersResource import AdminView20UsersResource
from Resources.Admin.AdminView20VehicleResource import AdminView20VehicleResource
from Resources.Admin.AdminViewPendingEditListingsResource import AdminViewPendingEditListingsResource
from Resources.Admin.AdminViewPendingNewListingsResource import AdminViewPendingNewListingsResource

from Resources.Comment.CommentAddResource import CommentAddResource
from Resources.Comment.CommentDeleteResource import CemmentDeleteResource
from Resources.Comment.CommentEditResource import CommentEditResource
from Resources.Comment.CommentViewSingleResource import CommentViewSingleResource

from Resources.Listing.ListingCreateResource import ListingCreateResource
from Resources.Listing.ListingDeleteResource import ListingDeleteResource
from Resources.Listing.ListingListResource import ListingListResource
from Resources.Listing.ListingSearhResource import ListingSearchResource
from Resources.Listing.ListingUnListResource import ListingUnListResource
from Resources.Listing.ListingUpdateResource import ListingUpdateResource
from Resources.Listing.ListingViewRandomRangePreviewResource import ListingViewRandomRangePreviewResource
from Resources.Listing.ListingViewResource import ListingViewResource

from Resources.User.UserDeleteResource import UserDeleteResource
from Resources.User.UserEditResource import UserEditResource
from Resources.User.UserLoginResource import UserLoginResource
from Resources.User.UserLogoutResource import UserLogoutResource
from Resources.User.UserRegisterResource import UserRegisterResource
from Resources.User.UserResetPasswordResource import UserResetPasswordResource
from Resources.User.UserViewAllListingsResource import UserViewAllListingsResource
from Resources.User.UserViewAllVehiclesResource import UserViewAllVehiclesResource
from Resources.User.UserViewProfileResource import UserViewProfileResource

from Resources.Vehicle.VehicleCreateResource import VehicleCreateResource
from Resources.Vehicle.VehicleDeleteResource import VehicleDeleteResource
from Resources.Vehicle.VehicleViewDetailsResource import VehicleViewDetailsResource

def load_api_endpoints(api):
    api.add_resource(AdminAcceptPendingEditListingResource, "admin/pending/edit/accept")
    api.add_resource(AdminAcceptPendingNewListingResource, "admin/pending/new/accept")
    api.add_resource(AdminAddNewRowToTableResource, "admin/new_row")
    api.add_resource(AdminDeleteCommentResource, "admin/delete/comment")
    api.add_resource(AdminDenyPendingEditListingResource, "admin/pending/edit/deny")
    api.add_resource(AdminDenyPendingNewListingResource, "admin/pending/new/deny")
    api.add_resource(AdminView20CommentResource, "admin/view/comment")
    api.add_resource(AdminView20ListingResource, "admin/view/listing")
    api.add_resource(AdminView20UsersResource, "admin/view/user")
    api.add_resource(AdminView20VehicleResource, "admin/view/vehicle")
    api.add_resource(AdminViewPendingEditListingsResource, "admin/pending/edit/view")
    api.add_resource(AdminViewPendingNewListingsResource, "admin/pending/new/view")
    api.add_resource(CommentAddResource, "comment/add")
    api.add_resource(CemmentDeleteResource, "comment/delete")
    api.add_resource(CommentEditResource, "comment/edit")
    api.add_resource(CommentViewSingleResource, "comment/view")
    api.add_resource(ListingCreateResource, "listing/create")
    api.add_resource(ListingDeleteResource, "listing/delete")
    api.add_resource(ListingListResource, "listing/list")
    api.add_resource(ListingSearchResource, "listing/search")
    api.add_resource(ListingUnListResource, "listing/unlist")
    api.add_resource(ListingUpdateResource, "listing/update")
    api.add_resource(ListingViewRandomRangePreviewResource, "listing/view/preview/random")
    api.add_resource(ListingViewResource, "listing/view")
    api.add_resource(UserDeleteResource, "user/delete")
    api.add_resource(UserEditResource, "user/edit")
    api.add_resource(UserLoginResource, "user/auth/login")
    api.add_resource(UserLogoutResource, "user/auth/logout")
    api.add_resource(UserRegisterResource, "user/auth/register")
    api.add_resource(UserResetPasswordResource, "user/auth/reset_password")
    api.add_resource(UserViewAllListingsResource, "user/view/listing/all")
    api.add_resource(UserViewAllVehiclesResource, "user/view/vehicle/all")
    api.add_resource(UserViewProfileResource, "user/view/profile")
    api.add_resource(VehicleCreateResource, "vehicle/create")
    api.add_resource(VehicleDeleteResource, "vehicle/delete")
    api.add_resource(VehicleViewDetailsResource, "vehicle/view")
