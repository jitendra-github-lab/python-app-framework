"""OpenAPI v3 Specification"""

# apispec via OpenAPI
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from marshmallow import Schema, fields

# Create an APISpec
spec = APISpec(
    title="{{cookiecutter.project_name}}",
    version="{{cookiecutter.Version}}",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)


# Define schemas
class ExampleOneOutput(Schema):
    msg = fields.String(description="Response will come as JSON", required=True)

# register example_one schemas with spec
spec.components.schema("Output", schema=ExampleOneOutput)

class ExampleTwoInput(Schema):
    name = fields.String(description="Request as JSON", required=True)

class ExampleTwoOutput(Schema):
    msg = fields.String(description="Response will come as JSON", required=True)

# register example_one schemas with spec
spec.components.schema("ExampleTwoInput", schema=ExampleTwoInput)
spec.components.schema("ExampleTwoOutput", schema=ExampleTwoOutput)

# add swagger tags that are used for endpoint annotation
# tags = [
#             {'name': 'Test Get functions',
#              'description': 'For testing the API.'
#             },
#             {'name': 'Test Post functions',
#              'description': 'Functions for getting response from POST method.'
#             },
#        ]

# for tag in tags:
#     print(f"Adding tag: {tag['name']}")
#     spec.tag(tag)