import os
import logging

from sqlalchemy import inspect, schema
from flasgger import Swagger
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import firebase_admin
from firebase_admin import credentials

logger = logging.getLogger(__name__)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://docker:' + os.getenv('POSTGRES_PWD') + '@' + os.getenv('POSTGRES_HOST') + \
                                        ':' + os.getenv('POSTGRES_PORT') + '/simple_project'

api = Api(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)

Swagger(app)

# Modules 

from simple_project.models import Something

try:
    Something.all()
except Exception as e:
    logger.info('Creating DB')
    logger.info(e)
    # Get schemas
    ins = inspect(db.engine)
    if 'public' not in ins.get_schema_names():
        # Create public schema if none
        db.engine.execute(schema.CreateSchema('public'))

    # Build tables
    db.create_all()
    db.session.commit()

# Resources

from simple_project.resources import SomethingResource

api.add_resource(
        SomethingResource, '/main_resource'
    )