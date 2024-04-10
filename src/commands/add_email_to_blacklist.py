from abc import ABC

from .base_command import BaseCommand
from ..models.model import db
from ..models.email import Email, ModelSchema
from ..commons.validation_util import validate_not_blank, validate_user_identity, validate_uuid, validate_email
from src.errors.errors import EmailAlreadyExits


class AddEmailToBlacklist(BaseCommand, ABC):
    def __init__(self, email, app_uuid, blocked_reason, ip, token):
        self.email = email
        self.app_uuid = app_uuid
        self.blocked_reason = blocked_reason
        self.ip = ip
        self.token = token

    def execute(self):
        validate_user_identity(self.token)
        validate_not_blank(self.email, self.app_uuid, self.blocked_reason, self.ip)
        validate_uuid(self.app_uuid)
        validate_email(self.email)
        email = Email.query.filter(Email.email == self.email).first()
        if email:
            raise EmailAlreadyExits
        email = Email(
            email=self.email,
            app_uuid=self.app_uuid,
            blocked_reason=self.blocked_reason,
            ip=self.ip)
        db.session.add(email)
        db.session.commit()
        return ModelSchema().dump(email)
