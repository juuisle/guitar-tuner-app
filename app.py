import os

from flask_cors import CORS
from flask import Flask, jsonify, render_template
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

from db import db
from ma import ma
from blacklist import BLACKLIST
from marshmallow import ValidationError
from resources.user import UserRegister, User, UserLogin, UserLogout, TokenRefresh
from resources.song import SongsList, Song
from resources.tuning import Tuning, TuningList, TuningSelected

app = Flask(__name__)

load_dotenv(".env", verbose=True)
# load default config from default_config.py
app.config.from_object("default_config")
app.config.from_envvar(
    "APPLICATION_SETTINGS"
)  # override with config.py (APPLICATION_SETTINGS points to config.py)

api = Api(app)
CORS(app)


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
api.add_resource(Tuning, "/tuning", "/tuning/<int:tuning_id>")
api.add_resource(TuningSelected, "/selected", "/selected/<int:tuning_id>")

api.add_resource(UserRegister, "/register")
api.add_resource(User, "/user/<int:user_id>")
api.add_resource(UserLogin, "/login")
api.add_resource(TokenRefresh, "/refresh")
api.add_resource(UserLogout, "/logout")


@app.route("/")
def documentation():
    return render_template("doc.html")


if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000, debug=True)
