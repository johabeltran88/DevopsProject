from flask import jsonify, request, Blueprint
from ..commands.add_email_to_blacklist import AddEmailToBlacklist
from ..commands.get_all import GetAll
from ..commands.is_email_in_blacklist import IsEmailInBlacklist

controller_blueprint = Blueprint('controller', __name__)


@controller_blueprint.route('/blacklists', methods=['POST'])
def add_email_to_blacklist():
    result = AddEmailToBlacklist(
        request.get_json().get('email', None),
        request.get_json().get('app_uuid', None),
        request.get_json().get('blocked_reason', None),
        request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0],
        request.headers.get('Authorization', None),
    ).execute()
    return jsonify(result), 201


@controller_blueprint.route('/blacklists', methods=['GET'])
def get_emails():
    result = GetAll(
        request.headers.get('Authorization', None)
    ).execute()
    return jsonify(result)


@controller_blueprint.route('/blacklists/<string:email>', methods=['GET'])
def is_email_in_blacklist(email):
    result = IsEmailInBlacklist(
        email,
        request.headers.get('Authorization', None)
    ).execute()
    return jsonify(result)


@controller_blueprint.route("/healthcheck", methods=['GET'])
def healthcheck():
    return jsonify('Service up!'), 200
