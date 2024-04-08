from abc import ABC

from .base_command  import  BaseCommand
from ..models.model import db
from ..models.email import Email, ModelSchema
from ..commons.validation_util import validate_not_blank, validate_user_identity

class  Create(BaseCommand, ABC):
	def  __init__(self, email, app_id, motivo, ip, token):
		self.email  =  email
		self.app_id = app_id
		self.motivo = motivo
		self.ip = ip
		self.token = token
		
	def  execute(self):
		validate_user_identity(self.token)
		validate_not_blank(self.email, self.app_id, self.motivo, self.ip)		
		email = Email(
			email = self.email,
			appId = self.app_id,
			motivo = self.motivo,
			ip = self.ip
		)
		db.session.add(email)
		db.session.commit()
		return ModelSchema().dump(email)