from flask import request, jsonify, Blueprint

from service.restaurant_service import RestaurantService


class RestaurantView:
    app = Blueprint('restaurant', __name__, url_prefix='/restaurants')

    @app.route('/', methods=['POST'])
    def create_restaurant():
        restaurant_service = RestaurantService()

        new_restaurant = request.json()

        new_restaurant_id = restaurant_service.create_restaurant(new_restaurant)

        new_restaurant = restaurant_service.get_restaurant(new_restaurant_id)

        return jsonify(new_restaurant)

    @app.route('/', methods=['GET'])
    def get_restaurant():
        restaurant_id = request.args.get('id')

        restaurant_service = RestaurantService()

        restaurant = restaurant_service.get_restaurant(restaurant_id)

        return jsonify(restaurant)

