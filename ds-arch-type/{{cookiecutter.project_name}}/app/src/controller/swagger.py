"""Definition of the Swagger UI Blueprint."""

from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/{{cookiecutter.project_name}}/docs'
API_URL = "/{{cookiecutter.project_name}}/swagger.json"

# Call factory function to create our blueprint
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "{{cookiecutter.project_name}}"
    }
)