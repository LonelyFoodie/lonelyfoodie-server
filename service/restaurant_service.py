from model import restaurant_dao


class RestaurantService:
    def __init__(self):
        self.restaurant_dao = restaurant_dao.RestaurantDao()

    def get_restaurant(self, new_restaurant_id):
        restaurant = self.restaurant_dao.select(new_restaurant_id)

        return restaurant

    def create_restaurant(self, new_restaurent):
        new_restaurant_id = self.restaurant_dao.insert(new_restaurent)

        return new_restaurant_id
