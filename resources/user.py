from flask import request
from flask_restful import Resource

from werkzeug.security import safe_str_cmp
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_refresh_token_required,
    get_jwt_identity,
    get_raw_jwt,
    jwt_required,
)
from marshmallow import ValidationError
from models.user import UserModel
from schemas.user import UserSchema
from blacklist import BLACKLIST

ERROR_BLANK = " '{}' field cannot be blank"
ERROR_INSERTING = "An error occurred inserting the song"
ERROR_USER_ALREADY_EXISTS = "An user with name '{}' already exist"
ERROR_USER_NOT_FOUND = "Tuning not found"
ERROR_INVALID_CREDENTIALS = "Invalid credentials"
MESSAGE_TUNNING_DELETED = "Tuning deleted"
MESSAGE_USER_CREATED = "User create successfully"
MESSAGE_USER_LOGGED_IN = "Login successfully"
MESSAGE_USER_LOGGED_OUT = "User <id={}> logged out"
MESSAGE_USER_DELETED = "User has been removed"

user_schema = UserSchema()


class UserRegister(Resource):
    @classmethod
    def post(cls):
        try:
            user = user_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400

        if UserModel.find_by_username(user.username):
            return ({"error": ERROR_USER_ALREADY_EXISTS.format(user.username)}, 400)

        user.save_to_db()

        return {"message": MESSAGE_USER_CREATED}, 201


class User(Resource):
    @classmethod
    def get(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"error": ERROR_USER_NOT_FOUND}, 404
        return user_schema.dump(user), 200

    @classmethod
    def delete(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"error": ERROR_USER_NOT_FOUND}, 404
        user.delete_from_db()
        return {"message": MESSAGE_USER_DELETED}, 200


class UserLogin(Resource):
    @classmethod
    def post(cls):
        user_data = user_schema.load(request.get_json())
        user = UserModel.find_by_username(user_data.username)

        if user and safe_str_cmp(user.password, user_data.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)

            return {"access_token": access_token, "refresh_token": refresh_token}, 200

        return {"error": ERROR_INVALID_CREDENTIALS}, 401


class UserLogout(Resource):
    @classmethod
    @jwt_required
    def post(cls):
        jti = get_raw_jwt()["jti"]
        user_id = get_jwt_identity()
        BLACKLIST.add(jti)
        return {"message": MESSAGE_USER_LOGGED_OUT.format(user_id)}, 200


class TokenRefresh(Resource):
    @classmethod
    @jwt_refresh_token_required
    def post(cls):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {"access_token": new_token}, 200
