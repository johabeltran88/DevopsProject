from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy import Integer, String, DateTime
from sqlalchemy_utils import UUIDType, IPAddressType

from .model import Model, db

# Extender la clase Model proporcionada
class Email(db.Model, Model):
	__tablename__  =  'emails'
	appId  =  db.Column(UUIDType(binary=False))
	motivo  =  db.Column(db.String(255))
	email  =  db.Column(db.String(255))
	ip = db.Column(IPAddressType)
    

# Constructor
def  __init__(self, appId = None, motivo = None, email = None, ip = None):
	Model.__init__(self)
	self.appId  =  appId
	self.motivo = motivo
	self.email = email
	self.ip = ip


# Especificar los campos que estarán presentes al serializar el objeto como JSON.
class ModelSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Email
        load_instance = True