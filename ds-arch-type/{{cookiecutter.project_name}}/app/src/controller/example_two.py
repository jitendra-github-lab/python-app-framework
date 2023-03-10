from flask import Blueprint, request
from app.src.services.example_service_two import ServiceTwo

'''
Author: {{cookiecutter.Author}}
Email: {{cookiecutter.Email}}
Version: {{cookiecutter.Version}}
File Description = Please describe file related information here.
'''
eg_two = Blueprint('example_2', __name__)


@eg_two.route('/', methods=['POST'], strict_slashes=False)
def index():
    """
        ---
        post:
          description: Swagger api with post endpoint
          requestBody:
            required: true
            content:
                application/json:
                    schema: ExampleTwoInput
          responses:
            '200':
              description: call successful
              content:
                application/json:
                  schema: ExampleTwoOutput
          tags:
              - Test Post response from eg_two
        """
    data = request.get_json()

    obj = ServiceTwo()
    output = obj.service_method(data)
    return output
