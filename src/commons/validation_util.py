import os
import uuid
import re

from src.errors.errors import BadRequestException, TokenInvalid, NotToken


def validate_not_blank(*values):
    for field in values:
        if field is None:
            raise BadRequestException


def validate_user_identity(token):
    if not token:
        raise NotToken
    if token.split(" ")[1] != os.environ.get('TOKEN', '40797d32-4825-4391-a2c3-051ab9e79a77'):
        raise TokenInvalid


def validate_uuid(value):
    try:
        uuid_obj = uuid.UUID(str(value))
        return str(uuid_obj) == value
    except ValueError:
        raise BadRequestException


def validate_email(value):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(regex, value):
        raise BadRequestException
