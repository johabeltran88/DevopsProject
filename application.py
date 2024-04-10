import os

from flask import Flask, make_response

from src.controllers.controller import controller_blueprint
from src.errors.errors import ApiException
from src.models.model import db

db_user = os.environ.get('DB_USER', "postgres")
db_password = os.environ.get('DB_PASSWORD', "postgres")
db_host = os.environ.get('DB_HOST', "localhost")
db_port = os.environ.get('DB_PORT', "5432")
db_name = os.environ.get('DB_NAME', "monitor_email")
db_uri = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_SQLITE', db_uri)
application.register_blueprint(controller_blueprint)

app_context = application.app_context()
app_context.push()

db.init_app(application)
db.create_all()


@application.errorhandler(ApiException)
def handle_exception(exception):
    return make_response(''), exception.code
