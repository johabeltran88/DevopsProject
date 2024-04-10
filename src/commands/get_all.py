from abc import ABC

from .base_command import BaseCommand
from ..commons.validation_util import validate_user_identity
from ..models.email import Email, ModelSchema


class GetAll(BaseCommand, ABC):
    def __init__(self, token):
        self.token = token

    def execute(self):
        validate_user_identity(self.token)
        emails = Email.query.all()
        if not emails:
            return []
        else:
            return [ModelSchema().dump(email) for email in emails]
