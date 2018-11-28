from ma import ma
from models.string import StringModel
from models.tuning import TuningModel


class StringSchema(ma.ModelSchema):
    class Meta:
        model = StringModel
        include_fk = True
