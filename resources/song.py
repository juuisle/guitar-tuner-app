from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, fresh_jwt_required
from marshmallow import ValidationError
from models.song import SongModel
from schemas.song import SongSchema

ERROR_BLANK = " '{}' field cannot be blank"
ERROR_NAME_ALREADY_EXISTS = "An song with name '{}' already exist"
ERROR_INSERTING = "An error occurred inserting the song"
ERROR_SONG_NOT_FOUND = "Song not found"
MESSAGE_SONG_DELETED = "Song deleted"

song_schema = SongSchema()
song_list_schema = SongSchema(many=True)


class Song(Resource):
    @classmethod
    def get(cls, name: str):
        song = SongModel.find_by_name(name)
        if song:
            return song_schema.dump(song)
        return {"error": ERROR_SONG_NOT_FOUND}, 404

    @classmethod
    #    @fresh_jwt_required
    def post(cls, name: str):
        if SongModel.find_by_name(name):
            return {"error": ERROR_NAME_ALREADY_EXISTS.format(name)}, 400

        try:
            song_json = request.get_json()
            song_json["name"] = name
            song = song_schema.load(song_json)
        except ValidationError as arr:
            return err.messages, 400

        try:
            song.save_to_db()
        except:
            return {"error": ERROR_INSERTING}, 500

        return song_schema.dump(song), 201

    @classmethod
    #    @jwt_required
    def delete(cls, name: str):
        song = SongModel.find_by_name(name)
        if song:
            song.delete_from_db()
            return {"message": MESSAGE_SONG_DELETED}, 200
        return {"error": ERROR_SONG_NOT_FOUND.format(name)}

    @classmethod
    #    @fresh_jwt_required
    def put(cls, name: str):
        song_json = request.get_json()
        song = SongModel.find_by_name(name)

        if song:
            song.length = song_json["length"]
            song.lyrics = song_json["lyrics"]
        else:
            song_json["name"] = name

            song = song_schema.load(song_json)

        song.save_to_db()

        return song_schema.dump(song), 200


class SongsList(Resource):
    @classmethod
    def get(self):
        return {"songs": song_list_schema.dump(SongModel.find_all())}
