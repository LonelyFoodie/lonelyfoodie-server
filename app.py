from flask import Flask
from flask_cors import CORS
from flask_restplus import Api

from view.restaurant import restaurant_view


def create_app():
    app = Flask(__name__)
    api = Api(app)

    CORS(app)

    app.config.from_pyfile("config.py")

    app.register_blueprint(restaurant_view.app)
    api.add_namespace(restaurant_view.api, path='/restaurants')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', debug=True, port=5000)
