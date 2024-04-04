from flask import jsonify, request, Blueprint
from ..commands.create  import  Create
from ..commands.get import Detail

routes_blueprint  = Blueprint('emails', __name__)

@routes_blueprint.route('/blacklists', methods=['POST'])
def create_email():
    request_json = request.get_json()
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0]  # Simplified IP retrieval
    result = Create(
                    request_json.get('email', None),
                    request_json.get('app_id', None),
                    request_json.get('motivo', None),
                    client_ip,                    
                    request.headers.get('Authorization', None),
                    client_ip
                    ).execute()
    return jsonify({'id': result['id'], 'createdAt': result['createdAt'], 'email': result['email']}), 201
