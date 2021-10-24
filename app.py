from flask import Flask
from flask_cors import CORS

from view.restaurant import restaurant_view


def create_app():
    app = Flask(__name__)

    CORS(app)

    app.config.from_pyfile("config.py")

    restaurant = restaurant_view.RestaurantView()

    app.register_blueprint(restaurant.app)

    return app