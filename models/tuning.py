from typing import List

from db import db


class TuningModel(db.Model):
    __tablename__ = "tunings"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    str_one = db.Column(db.Float(precision=2), nullable=False)
    str_two = db.Column(db.Float(precision=2), nullable=False)
    str_three = db.Column(db.Float(precision=2), nullable=False)
    str_four = db.Column(db.Float(precision=2), nullable=False)
    str_five = db.Column(db.Float(precision=2), nullable=False)
    str_six = db.Column(db.Float(precision=2), nullable=False)

    songs = db.relationship("SongModel", lazy="dynamic")

    @classmethod
    def find_by_name(cls, name: str) -> "TuningModel":
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all(cls) -> List["TuningModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
