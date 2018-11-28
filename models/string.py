from typing import List

from db import db


class StringModel(db.Model):
    __tablename__ = "string"

    str_one = db.Column(db.Float(precision=2), nullable=False)
    str_two = db.Column(db.Float(precision=2), nullable=False)
    str_three = db.Column(db.Float(precision=2), nullable=False)
    str_four = db.Column(db.Float(precision=2), nullable=False)
    str_five = db.Column(db.Float(precision=2), nullable=False)
    str_six = db.Column(db.Float(precision=2), nullable=False)

    @classmethod
    def find_by_name(cls, name: str) -> "StringModel":
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all(cls) -> List["StringModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
