from typing import List

from db import db


class TuningModel(db.Model):
    __tablename__ = "tunings"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    songs = db.relationship("SongModel", lazy="dynamic")
    strings = db.relationship("StringModel", lazy="dynamic")

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
