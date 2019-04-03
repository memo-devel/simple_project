import logging
from simple_project import ma
from marshmallow import fields, ValidationError, post_load

logger = logging.getLogger(__name__)

class SimpleSchema(ma.Schema):
    name = fields.String(required=True, allow_none=False)
    value = fields.Integer(required=True, allow_none=False)

simple_schema = SimpleSchema()
simple_schema_list = SimpleSchema(many=True)