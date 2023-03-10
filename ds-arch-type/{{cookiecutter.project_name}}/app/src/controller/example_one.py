from flask import Blueprint, jsonify
from app.config.appconfig_parser import log_parser

'''
Author: {{cookiecutter.Author}}
Email: {{cookiecutter.Email}}
Version: {{cookiecutter.Version}}
File Description = Please describe file related information here.
'''

eg_one = Blueprint('example_1', __name__)
logger = log_parser().getChild("eg_one")


@eg_one.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    ---
    get:
      description: eg_one endpoint
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: ExampleOneOutput
      tags:
          - Test GET Response from example_one
    """
    output = 'Getting response from example_one index function.'
    return jsonify(output)


@eg_one.route('/index-two', methods=['GET'], strict_slashes=False)
def index_two():
    """
    ---
    get:
      description: eg_one endpoint
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: ExampleOneOutput
      tags:
          - swagger response from example_one index_two
    """
    logger.debug("GET Method index_two called")
    output = 'Getting response from example_one index_two function.'
    return jsonify(output)
    