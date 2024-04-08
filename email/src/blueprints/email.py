from flask import jsonify, request, Blueprint
from ..commands.create  import  Create
from ..commands.list  import  ListEmails
from ..commands.getEmail import GetEmail

emails_blueprint  = Blueprint('emails', __name__)

@emails_blueprint.route('/blacklists', methods=['POST'])
def create_email():
    request_json = request.get_json()
    print("Requests called")
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0]  # Simplified IP retrieval
    print("IP step")
    result = Create(
                    request_json.get('email', None),
                    request_json.get('app_id', None),
                    request_json.get('motivo', None),
                    client_ip,                    
                    request.headers.get('Authorization', None),
                    ).execute()
    print("Result step")
    return jsonify({'id': result['id'], 'createdAt': result['createdAt'], 'email': result['email']}), 201

@emails_blueprint.route('/blacklists', methods=['GET'])
def get_emails():
    request_json = request.get_json()
    result = ListEmails(
                    request.headers.get('Authorization', None)
                    ).execute()
    return jsonify({'id': result['id'], 'createdAt': result['createdAt'], 'email': result['email'], 'ip': result['ip']}), 200

@emails_blueprint.route('/blacklists/<string:email>', methods=['GET'])
def get_email(email):
    json = request.get_json()
    result = GetEmail(email, request.headers.get('Authorization', None)).execute()
    if not result:
        return jsonify({'existeEmail': False, 'Motivo': ''})
    return jsonify({'existeEmail': True, 'Motivo': result['motivo']})