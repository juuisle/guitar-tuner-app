from flask import request
from flask_jwt_extended import jwt_required, fresh_jwt_required
from flask_restful import Resource
from models.tuning import TuningModel
from schemas.tuning import TuningSchema
from marshmallow import ValidationError


ERROR_TUNNING_ALREADY_EXISTS = "An tuning with name '{}' already exist"
ERROR_INSERTING = "An error occurred inserting the tuning"
ERROR_TUNNING_NOT_FOUND = "Tuning not found"
MESSAGE_TUNNING_DELETED = "Tuning deleted"

tuning_schema = TuningSchema()
tuning_list_schema = TuningSchema(many=True)


class Tuning(Resource):
    @classmethod
    def get(cls, tuning_id: int):
        tuning = TuningModel.find_by_id(tuning_id)
        if tuning:
            return tuning_schema.dump(tuning), 200
        return {"error": ERROR_TUNNING_NOT_FOUND}, 404

    @classmethod
    def post(cls):
        try:
            tuning_json = request.get_json()
            tuning = tuning_schema.load(tuning_json)
        except ValidationError as err:
            return err.messages, 400

        if TuningModel.find_by_name(tuning.name):
            return ({"error": ERROR_TUNNING_ALREADY_EXISTS.format(tuning.name)}, 400)

        try:
            tuning.save_to_db()
        except:
            return {"error": ERROR_INSERTING}, 500

        return tuning_schema.dump(tuning), 201

    @classmethod
    def delete(cls, tuning_id: int):
        tuning = TuningModel.find_by_id(tuning_id)
        if tuning:
            tuning.delete_from_db()
            return {"message": MESSAGE_TUNNING_DELETED}, 200
        return {"error": ERROR_TUNNING_NOT_FOUND}, 401


class TuningList(Resource):
    @classmethod
    def get(cls):
        return tuning_list_schema.dump(TuningModel.find_all())


# There are logical bugs in this class.
class TuningSelected(Resource):
    @classmethod
    def get(cls):
        return {"selected": tuning_schema.dump(TuningModel.get_seleted())}

    @classmethod
    def post(cls, tuning_id: int):
        try:
            TuningModel.select_by_id(tuning_id)
        except:
            return {"error": ERROR_TUNNING_NOT_FOUND}, 500
        return cls.get()
