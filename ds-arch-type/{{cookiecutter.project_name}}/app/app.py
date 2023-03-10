from flask import Flask, jsonify, redirect, url_for
from app.schema import spec
from app.src.controller.swagger import swagger_ui_blueprint, SWAGGER_URL
from app.config.appconfig_parser import log_parser
import requests

'''
Author: {{cookiecutter.Author}}
Email: {{cookiecutter.Email}}
Version: {{cookiecutter.Version}}
File Description = Please describe file related information here.
'''
logger = log_parser().getChild("app")

def create_app():
   
    from app.src.controller.example_one import eg_one
    from app.src.controller.example_two import eg_two

    app = Flask("{{cookiecutter.project_name}}", static_folder="app/assets")

    # Register blueprints {{cookiecutter.project_name}}
    app.register_blueprint(eg_one, url_prefix='/{{cookiecutter.project_name}}/egone')
    app.register_blueprint(eg_two, url_prefix='/{{cookiecutter.project_name}}/egtwo')
    app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

    @app.route("/", strict_slashes=False)
    def _defatult():
        return "Your application server is healty :) !! "


    swagger_api(app)

    @app.errorhandler(404)
    @app.errorhandler(405)
    def page_not_found(ex):
        logger.error(str(ex))
        return jsonify(error=str(ex)), ex.code

    return app


def swagger_api(app):
    with app.test_request_context():
        # register all swagger documented functions here
        for fn_name in app.view_functions:
            if fn_name == 'static':
                continue
            print(f"Loading swagger docs for function: {fn_name}")
            view_fn = app.view_functions[fn_name]
            spec.path(view=view_fn)

    @app.route("/{{cookiecutter.project_name}}/swagger.json")
    def create_swagger_spec():
        return jsonify(spec.to_dict())

