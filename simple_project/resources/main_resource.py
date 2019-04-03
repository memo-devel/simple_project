import logging

from flask import request, g
from flask_restful import Resource

from simple_project.schemas import simple_schema
from simple_project.models import Something


logger = logging.getLogger(__name__)

class SomethingResource(Resource):
    def post(self):
        """
        Create Something
        ---
        tags:
          - Something
        parameters:
          - in: body
            name: body
            schema:
              id: PostSomething
              properties:
                name:
                  default: "Jhon"
                  description: Name of user to be created.
                  type: string
                  required: true
                value:
                   default: "Doe"
                   description: Last name of user.
                   type: string
                   required: true

        responses:
          201:
            description: A list of employees
          401:
            description: Token is not valid
        """
        req = request.get_json()
        user_sch = simple_schema.load(req)
        if len(user_sch.errors) > 0:
            logger.error(user_sch.errors)
            return 'Format input error.', 400

        Something.add_one(**user_sch.data)
        return 'Success', 200

    def get(self):
        """
        List Something
        ---
        tags:
          - Something
        """
        usr_sch_d = simple_schema.dump(Something.all())
        return usr_sch_d.data, 200
