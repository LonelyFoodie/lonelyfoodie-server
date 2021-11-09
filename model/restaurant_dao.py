from flask_restplus import Namespace, fields


class RestaurantDao:
    api = Namespace('Restaurant', description='restaurant related operations')
    restaurant = api.model('restaurant', {
        'id': fields.String(required=True, description='Restaurant ID')
    })

    def __init__(self):
        self.db = None

    def select(self, restaurant):
        return {'id': 'test_id'}

    def insert(self, restaurant):
        return 'test_id'

    def update(self, restaurant):
        pass

    def delete(self, restaurant):
        pass