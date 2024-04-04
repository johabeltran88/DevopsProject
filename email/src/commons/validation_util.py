from src.errors.errors import BadRequestException, FlightIdAlreadyExits, InvalidDate, TokenInvalid, NotToken
from ..models.model import db
from ..models.email import Email
from datetime import datetime, date
import uuid
import os


def validate_not_blank(*fields):
    for field in fields:
        if field is None:
            raise BadRequestException


def validate_at_least_one_not_blank(*fields):
    for field in fields:
        if field is not None:
            return
    raise BadRequestException

def validate_user_identity(received_token):
    expected_token = os.environ.get('TOKEN', None)
    
    if not expected_token or received_token != expected_token:
        raise TokenInvalid
    
def validate_values_UUID(variable):
    try:
        uuid_obj = uuid.UUID(str(variable))
        return str(uuid_obj) == variable
    except ValueError:
        raise BadRequestException    
