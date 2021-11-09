from flask import request, jsonify, Blueprint
from flask_restplus import Namespace, Resource, fields

from service.restaurant_service import RestaurantService

app = Blueprint('Restaurant', __name__, url_prefix='/restaurants')
api = Namespace('Restaurant', description='Restaurant related operations')


restaurant = api.model('Restaurant', {
    'id': fields.String(required=True, description='identifier')
})


@api.route('/<id>')
class Restaurant(Resource):

    @app.route('/', methods=['POST'])
    def post(self):
        restaurant_service = RestaurantService()

        new_restaurant = request.json()

        new_restaurant_id = restaurant_service.create_restaurant(new_restaurant)

        new_restaurant = restaurant_service.get_restaurant(new_restaurant_id)

        return jsonify(new_restaurant)

    @api.doc('restaurant')
    @api.marshal_with(restaurant)
    @app.route('/<id>', methods=['GET'])
    def get(self, id):
        restaurant_service = RestaurantService()

        restaurant = restaurant_service.get_restaurant(id)

        return jsonify(restaurant)
