from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy_utils import UUIDType, IPAddressType

from .model import Model, db


class Email(db.Model, Model):
    __tablename__ = 'emails'
    email = db.Column(db.String(255))
    app_uuid = db.Column(UUIDType(binary=False))
    blocked_reason = db.Column(db.String(255))
    ip = db.Column(IPAddressType)

    def __init__(self, email=None, app_uuid=None, blocked_reason=None, ip=None):
        Model.__init__(self)
        self.email = email
        self.app_uuid = app_uuid
        self.blocked_reason = blocked_reason
        self.ip = ip


class ModelSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Email
        load_instance = True
