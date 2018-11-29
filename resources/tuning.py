from flask import request
from flask_jwt_extended import jwt_required, fresh_jwt_required
from flask_restful import Resource
from models.tuning import TuningModel
from schemas.tuning import TuningSchema

ERROR_TUNNING_ALREADY_EXISTS = "An song with name '{}' already exist"
ERROR_INSERTING = "An error occurred inserting the song"
ERROR_TUNNING_NOT_FOUND = "Tuning not found"
MESSAGE_TUNNING_DELETED = "Tuning deleted"

tuning_schema = TuningSchema()
tuning_list_schema = TuningSchema(many=True)


class Tuning(Resource):
    @classmethod
    def get(cls, name: str):
        tuning = TuningModel.find_by_name(name)
        if tuning:
            return tuning_schema.dump(tuning), 200
        return {"error": ERROR_TUNNING_NOT_FOUND}, 404

    @classmethod
    def post(cls, name: str):
        if TuningModel.find_by_name(name):
            return ({"error": ERROR_TUNNING_ALREADY_EXISTS.format(name)}, 400)

        tuning = TuningModel(name=name)
        try:
            tuning.save_to_db()
        except:
            return {"error": ERROR_INSERTING}, 500

        return tuning_schema.dump(tuning), 201

    @classmethod
    def delete(cls, name: str):
        tuning = TuningModel.find_by_name(name)
        if tuning:
            tuning.delete_from_db()
            return {"message": MESSAGE_TUNNING_DELETED}, 200
        return {"error": ERROR_TUNNING_NOT_FOUND}, 401


class TuningList(Resource):
    @classmethod
    def get(self):
        return {"tunings": tuning_list_schema.dump(TuningModel.find_all())}


class TunningSelected(Resource):
    @classmethod
    def get(self):
        return {"tuning": "default tuning"}

    @classmethod
    def post(self):
        return {"post succeeded!"}
