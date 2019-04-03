from simple_project import db
import logging

logger = logging.getLogger(__name__)

class Something(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    value = db.Column(db.Integer())

    @classmethod
    def find(cls, name):
        data = cls.query.filter_by(name=name).all()
        return spec

    @classmethod
    def add_one(cls, **kwargs):
        spec = cls(**kwargs)
        db.session.add(spec)
        db.session.commit()
        return spec

    @classmethod
    def all(cls, name):
        data = cls.query.all()
        return spec
