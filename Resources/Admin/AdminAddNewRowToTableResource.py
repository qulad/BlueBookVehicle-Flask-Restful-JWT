from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import get_tablename_rowname_brandid_modelid, get_table_from_str
from Models import db
from Models.User.UserModel import User

class AdminAddNewRowToTableResource(Resource):
    """
    AdminAddNewRowToTableResource is used by admins to add new options for users to choose from.
    Use HTTP GET method.
    Request must contain:
        access_token,
        table name,
        new row name.
    Request constrains:
        access_token must be linked to an existing admin in the database,
        table name must be a tables name in the database.
    Responses:
        access_token is not linked to anyone:
            Response message: Your account can't be found.
            Response code: 404
        user does not have admin privilages:
            Response message: You don't have admin priviliges.
            Response code: 403
        table name in not a table:
            Response message: Table not found.
            Response code: 404
        brand_id is missing:
            Response message: Argument 'brand_id' is absent.
            Response code: 400
        model_id is missing:
            Response message: Argument 'model_id' is absent.
            Response code: 400
        row added to table:
            Response message: You have successfully added a row to table.
            Response code: 201
    """
    @jwt_required()
    def get(self):
        table_name, row_name, brand_id, model_id = get_tablename_rowname_brandid_modelid()
        
        current_user_id = get_jwt_identity()
        current_user = User.query.filter_by(user_id=current_user_id).first()
        if not current_user:
            return {"message": "Your account can't be found."}, 404
        admin_privalige = current_user.is_admin
        if not admin_privalige:
            return {"message": "You don't have admin priviliges."}, 403
        table = get_table_from_str(table_name)
        if table == -1:
            return {"message": "Table not found."}, 404

        if str(table) == "VehicleModel":
            if brand_id == None:
                return {"message": "Argument 'brand_id' is absent."}, 400
            new_row = table(brand_id=brand_id, model_type=row_name)
        elif str(table) == "VehicleMake":
            if model_id == None:
                return {"message": "Argument 'model_id' is absent."}, 400
            new_row = table(model_id=model_id, make_year=row_name)
        else:
            new_row = table(row_name)

        db.session.add(new_row)
        db.session.commit()
        return {"message": "You have successfully added a row to table."}, 201
    