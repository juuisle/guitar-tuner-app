from ma import ma
from models.song import SongModel
from models.tuning import TuningModel
from models.string import StringModel


class SongSchema(ma.ModelSchema):
    class Meta:
        model = SongModel
        load_only = ("tuning",)
        dump_only = ("id",)
        include_fk = True
