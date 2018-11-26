from typing import List

from db import db


class SongModel(db.Model):
    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    length = db.Column(db.Float(precision=2), nullable=False)
    lyrics = db.Column(db.Text, nullable=True)

    tuning_id = db.Column(db.Integer, db.ForeignKey("tunings.id"), nullable=False)
    tuning = db.relationship("TuningModel")

    @classmethod
    def find_by_name(cls, name: str) -> "SongModel":
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all(cls) -> List["SongModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
