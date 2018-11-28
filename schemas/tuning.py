from ma import ma

from models.tuning import TuningModel
from models.song import SongModel
from schemas.song import SongSchema
from schemas.string import StringSchema


class TuningSchema(ma.ModelSchema):
    songs = ma.Nested(SongSchema, many=True)
    strings = ma.Nested(StringSchema, many=True)

    class Meta:
        model = TuningModel
        dump_only = ("id",)
        include_fk = True
