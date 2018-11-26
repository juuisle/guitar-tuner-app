import os

from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager

from db import db
from ma import ma
from blacklist import BLACKLIST
from marshmallow import ValidationError
from resources.user import UserRegister, User, UserLogin, UserLogout, TokenRefresh
from resources.song import SongsList, Song
from resources.tuning import Tuning, TuningList

app = Flask(__name__)

user_dataBASE = os.environ.get("user_dataBASE_URL", "sqlite:///user_data.db")

app.config["SQLALCHEMY_user_dataBASE_URI"] = user_dataBASE
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTION"] = True
app.config["JWT_BLACKLIST_ENABLED"] = True
app.config["JWT_BLACKLIST_TOKEN_CHECKS"] = ["access", "refresh"]

app.config["JWT_SECRET_KEY"] = "very-handsome"
api = Api(app)

if user_dataBASE == "sqlite:///user_data.db":

    @app.before_first_request
    def create_tables():
        db.create_all()


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400


jwt = JWTManager(app)


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    return decrypted_token["jti"] in BLACKLIST


@jwt.invalid_token_loader
def invalid_token_callback(error):
    return (
        jsonify(
            {"description": "Signature verification failed.", "error": "invalid_token"}
        ),
        401,
    )


@jwt.unauthorized_loader
def missing_token_callback(error):
    return (
        jsonify(
            {
                "description": "Request does not contain an access token.",
                "error": " authoried_required",
            }
        ),
        401,
    )


@jwt.needs_fresh_token_loader
def token_not_fresh_callback(error):
    return (
        jsonify(
            {"description": "The token is not fresh.", "error": " fresh_token_required"}
        ),
        401,
    )


@jwt.revoked_token_loader
def revoked_token_callback():
    return (
        jsonify(
            {"description": "The token has been revoked.", "error": " token_revoked"}
        ),
        401,
    )


api.add_resource(TuningList, "/tunings")
api.add_resource(SongsList, "/songs")
api.add_resource(Song, "/song/<string:name>")
api.add_resource(Tuning, "/tuning/<string:name>")

api.add_resource(UserRegister, "/register")
api.add_resource(User, "/user/<int:user_id>")
api.add_resource(UserLogin, "/login")
api.add_resource(TokenRefresh, "/refresh")
api.add_resource(UserLogout, "/logout")

if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000, debug=True)
