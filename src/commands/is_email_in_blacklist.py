from abc import ABC

from .base_command import BaseCommand
from ..commons.validation_util import validate_user_identity, validate_email
from ..models.email import Email


class IsEmailInBlacklist(BaseCommand, ABC):
    def __init__(self, email, token):
        self.email = email
        self.token = token

    def execute(self):
        validate_user_identity(self.token)
        validate_email(self.email)
        email = Email.query.filter(Email.email == self.email).first()
        if email:
            return {'is_in_blacklist': True, 'blocked_reason': email.blocked_reason}
        return {'is_in_blacklist': False, 'blocked_reason': None}
