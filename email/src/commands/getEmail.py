from abc import ABC
from .base_command  import  BaseCommand
from ..models.model import db
from ..models.email import Email, ModelSchema
from ..commons.validation_util import validate_user_identity

class GetEmail(BaseCommand, ABC):
    def __init__(self, email, token):
        self.email = email
        self.token = token
    
    def execute(self):
        validate_user_identity(self.token)
        email = Email.query.filter(Email.email == self.email).first()
        if not email:
            return None
        
        return ModelSchema().dump(email)