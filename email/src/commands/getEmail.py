from abc import ABC
from .base_command  import  BaseCommand
from ..models.model import db
from ..models.email import Email, ModelSchema

class GetEmail(BaseCommand, ABC):
    def __init__(self, email, token):
        self.email = email
        self.token = token
    
    def execute(self):
        email = Email.query.filter(Email.email == self.email).first()
        if not email:
            return None
        
        return ModelSchema().dump(email)